#!/usr/bin/python
# -*- coding: utf-8 -*-

#import socket
import logging, sys, os, os.path
from PyQt4 import QtCore, QtGui

from Crypto.Hash import SHA512, MD5
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.PublicKey import RSA

from main import Ui_MainWindow
from ImportDialog import Ui_ImportDialog
from ExportDialog import Ui_ExportDialog
#from NewRsaDialog import Ui_NewRsaDialog
from GetRsaDialog import Ui_GetRsaDialog
from GetRsaDialogCreate import Ui_GetRsaDialogCreate
from GetRsaDialogImport import Ui_GetRsaDialogImport
from GetRsaDialogResult import Ui_GetRsaDialogResult
from GetRsaDialogShow import Ui_GetRsaDialogShow

import urllib

from datetime import datetime
import time

import ast

from identicon import generate_identicon

#try:
    #_fromUtf8 = QtCore.QString.fromUtf8
#except AttributeError:
    #_fromUtf8 = lambda s: s

LOGGER = None
LOG_LEVEL = 'INFO'
LOG_FILE_PATH = 'tai.log'
LOG_CONSOLE_FORMAT = '%(asctime)s [%(levelname)s] %(message)s'
LOG_FILE_FORMAT = '%(asctime)s [%(levelname)s] %(message)s'

COLECTION_PATH = '../data/colections'
IDENTICON_PATH = '../data/img/identicons'
RSAKEY_PATH = '../data/rsa'
RSAKEY_PUB_PATH = '../data/rsa.pub'
FRIENDS_PATH = '../data/friends'
IMAGES_PATH = '../data/img'

FILES = {}
FRIENDS = {}

RSAKEY = None
KEY_ID = None
KEY_IDENTICON = None
KEY_IDENTICON_24 = None


def create_rsapub_file(rsakey_file_paht, rsakey):
    rsakey_file = open(rsakey_file_paht,'w')
    rsakey_file.write(rsakey.publickey().exportKey('PEM'))

    
def generate_rsakey(length):
    random_generator = Random.new().read
    return RSA.generate(length, random_generator)


def load_global_files():
    global FILES
    FILES = {}
    for file in os.listdir(COLECTION_PATH):
        if os.path.isdir(os.path.join(COLECTION_PATH,file)):
            FILES[file] = []
            
    for colection in FILES:
        for file in os.listdir(os.path.join(COLECTION_PATH, colection)):
            if not os.path.isdir(os.path.join(COLECTION_PATH, colection,file)):
                FILES[colection].append(file)


def load_global_friends():
    global FRIENDS
    FRIENDS = {}
    for friend in os.listdir(FRIENDS_PATH):
        if not os.path.isdir(os.path.join(FRIENDS_PATH,friend)):
            key_file = open(os.path.join(FRIENDS_PATH,friend))
            alias = friend[32:]
            id = friend[:32]
            try:
                FRIENDS[id] = (alias, RSA.importKey(key_file.read()))
            except ValueError:
                print('Can not import ' + friend + '\'s key')

                
def update_global_friend_alias(key, alias):
    global FRIENDS
    rsakey = FRIENDS[key][1]
    FRIENDS[key] = (alias, rsakey)


def load_global_rsakey_data(rsakey, key_id, key_identicon, key_identicon_24):
    global RSAKEY
    global KEY_ID
    global KEY_IDENTICON
    global KEY_IDENTICON_24
    (RSAKEY, KEY_ID, KEY_IDENTICON, KEY_IDENTICON_24) = (rsakey,
                                                         key_id, key_identicon,
                                                         key_identicon_24
                                                        )

def get_friend_displayname(id):
    global FRIENDS
    alias = FRIENDS[id][0]
    if alias == '':
        alias = id
    return alias
    
    
def get_rsakey_id(key):
    return MD5.new(SHA512.new(key.exportKey()).hexdigest()).hexdigest()


def create_identicon(user_id):
    generate_identicon(user_id,7,os.path.join(IDENTICON_PATH, user_id)+'.png')
    
    #try:
        ##urllib.urlretrieve('http://identicon.org/?t=' + user_id + '&s=24',
        #urllib.urlretrieve('http://permissiondenied.net/identicon/64/' +user_id + '.png', os.path.join(IDENTICON_PATH, user_id))
    #except IOError:
        #pass


def get_identicon_pixmap(user_id):
    image_path = os.path.join(IDENTICON_PATH,user_id)
    if os.path.exists(image_path):
        return QtGui.QPixmap(os.path.join(IDENTICON_PATH,user_id))
    else:
        create_identicon(user_id)
        return QtGui.QPixmap(os.path.join(IDENTICON_PATH,user_id))


def get_identicon_24_pixmap(user_id):
    try:
        return get_identicon_pixmap(user_id).scaled(24, 24, 1, 1)
    except IOError:
        pass

8192


def import_encrypt_file(input_file_path, output_file_path, rsa, key_length):
    bs = AES.block_size
    
    key = Random.new().read(key_length)
    iv = 'aaaaaaaaaaaaaaaa'
    
    encrypted_key = rsa.encrypt(key,None)[0]
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    finished = False
    
    input_file_handler = open(input_file_path, 'rb')
    output_file_handler = open(output_file_path, 'wb')
    
    while not finished:
        chunk = input_file_handler.read(1024 * bs)
        if len(chunk) == 0 or len(chunk) % bs != 0:
            padding_length = (bs - len(chunk) % bs) or bs
            chunk += padding_length * chr(padding_length)
            finished = True
        output_file_handler.write(cipher.encrypt(chunk))
    
    
    output_file_handler.close()
    input_file_handler.close()
        
    hash = get_file_sha512(input_file_path)
    signature = rsa.sign(hash, None)
    
    output_file_handler = open(output_file_path, 'r+')
    file_header = create_header({'encrypt_key': encrypted_key,
                   'aes_key_length': key_length,
                   'author': KEY_ID,
                   'signature': signature,
                   'input_date': time.mktime(datetime.now().timetuple()),
                   'share_date': None,
                   'import_date': time.mktime(datetime.now().timetuple())
                  })
    
    lines = output_file_handler.readlines()
    output_file_handler.seek(0)
    output_file_handler.write(file_header)
    output_file_handler.writelines(lines) 
    
    output_file_handler.close()

def export_decrypt_file(input_file_path, output_file_path, rsa):
    bs = AES.block_size
    
    input_file_handler = open(input_file_path, 'rb')
    input_file_header = extract_file_header(input_file_handler)
    encrypted_key = input_file_header['encrypt_key']
    
    key = rsa.decrypt(encrypted_key)
    iv = 'aaaaaaaaaaaaaaaa'
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    next_chunk = ''
    finished = False
    output_file_handler = open(output_file_path, 'wb')
    while not finished:
        chunk, next_chunk = (next_chunk,
                            cipher.decrypt(input_file_handler.read(1024 * bs)))
        if len(next_chunk) == 0:
            padding_length = ord(chunk[-1])
            chunk = chunk[:-padding_length]
            finished = True
        output_file_handler.write(chunk)
        
    input_file_handler.close()
    output_file_handler.close()

        
def create_header(dict):
    s_dict = str(dict)
    if len(s_dict) < 4294967296:
        return '%08x%s' % (len(s_dict), s_dict)
    else:
        raise ValueError('Literal string from input dictionary cannot be longer than 4294967296 bytes (4GiB)')


def get_file_header(file):
    file_ = file
    return extract_file_header(file_)


def extract_file_header(file):
    header_len = int(file.read(8), 16)
    header_str = file.read(header_len)
    return ast.literal_eval(header_str)


def get_file_sha512(path, block_size=256*128):
    sha512 = SHA512.new()
    with open(path,'rb') as f: 
        for chunk in iter(lambda: f.read(block_size), b''): 
             sha512.update(chunk)
    return sha512.hexdigest()
#class Header():
    #def __init__(self, dict=[], file=None):
        #_elements = dict
        #if file:
            #get_file_header(file)os.path.join


    #def add_value(self,field, value):
        #s_field, s_value = str(field), str(value)
        #self._elements[s_field] = s_value


    #def __str__(self)
        #s_elements = str(_elements):
        #if len(s_elements) < 4294967296:
            #return '%08x%s' % (len(s_elements), s_elements)
        #else:
            #raise ValueError('Literal string from input dictionary cannot be longer than 4294967296 bytes')


    #def get_file_header(self,file):
        #file_ = file
        #extract_file_header(file_)


    #def extract_file_header(self,file):
        #header_len = file.read(8)
        #header
    


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        
        
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.load_program()
        
        #self.ui.keyid.setText(KEY_ID)
        
        #self.ui.identicon.setPixmap(KEY_IDENTICON_24)
        
        self.colection_tree_update()
        self.friend_list_update()
        
        ##FRIEND_MENU
            ##ACTIONS
        #self.ui.actionFriendShare = QtGui.QAction(self)
        #self.ui.actionFriendShare.setIcon(QtGui.QIcon.fromTheme('document-share'))
        #self.ui.actionFriendShare.setObjectName('actionFriendShare')
        #self.ui.actionFriendShare.setText(QtGui.QApplication.translate('MainWindow', 'Share', None, QtGui.QApplication.UnicodeUTF8))
        
        #self.ui.actionFriendAdd = QtGui.QAction(self)
        #self.ui.actionFriendAdd.setIcon(QtGui.QIcon.fromTheme('list-add-user'))
        #self.ui.actionFriendAdd.setObjectName('actionFriendAdd')
        #self.ui.actionFriendAdd.setText(QtGui.QApplication.translate('MainWindow', 'Add', None, QtGui.QApplication.UnicodeUTF8))
        
        #self.ui.actionFriendRemove = QtGui.QAction(self)
        #self.ui.actionFriendRemove.setIcon(QtGui.QIcon.fromTheme('list-remove-user'))
        #self.ui.actionFriendRemove.setObjectName('actionFriendRemove')
        #self.ui.actionFriendRemove.setText(QtGui.QApplication.translate('MainWindow', 'Remove', None, QtGui.QApplication.UnicodeUTF8))
        
            ##ACTIONS
        #self.ui.friendMenu = QtGui.QMenu(self.ui.friendsList)
        #self.ui.friendMenu.setObjectName(_fromUtf8('friendMenu'))
        
        
        #self.ui.friendMenu.addAction(self.ui.actionFriendShare)
        #self.ui.friendMenu.addSeparator()
        #self.ui.friendMenu.addAction(self.ui.actionFriendAdd)
        #self.ui.friendMenu.addAction(self.ui.actionFriendRemove)
        
        
            
            #self.connect(self.ui.colectionTree,
                         #QtCore.SIGNAL('itemClicked()'),
                         #self.show_item
                        #)
                        
                        
                        
            #self.ui.model = QStandardItemModel()
            
            #self.ui.colectionTree..setModel(self.model)
            
            #self.treeView.setModel(self.model)
            #self.model.appendRow(QStandardItem('<bHello</b'))
            #self.model.appendRow(QStandardItem('World'))
        
        
        self.ui.colection.addItems(FILES.keys())
        self.update_file(self.ui.colection.currentText())
        
        self.ui.action_file_read.setIcon(QtGui.QIcon.fromTheme('document-open'))
        self.ui.action_file_import.setIcon(QtGui.QIcon.fromTheme('document-import'))
        self.ui.action_file_export.setIcon(QtGui.QIcon.fromTheme('document-export'))
        
        self.ui.action_colection_newcolection.setIcon(QtGui.QIcon.fromTheme('list-add'))
        self.ui.action_collection_removecollection.setIcon(QtGui.QIcon.fromTheme('list-remove'))
        
        self.ui.action_friends_add.setIcon(QtGui.QIcon.fromTheme('list-add-user'))
        
        self.ui.action_view_panels_colections.setIcon(QtGui.QIcon.fromTheme('folder'))
        self.ui.action_view_panels_friends.setIcon(QtGui.QIcon.fromTheme('user-identity'))
        
        self.ui.action_contextualfriend_add.setIcon(QtGui.QIcon.fromTheme('list-add-user'))
        self.ui.action_contextualfriend_remove.setIcon(QtGui.QIcon.fromTheme('list-remove-user'))
        self.ui.action_contextualfriend_share_external.setIcon(QtGui.QIcon.fromTheme('document-import'))
        self.ui.action_contextualfriend_show.setIcon(QtGui.QIcon.fromTheme('view-form'))
        self.ui.action_contextualfriend_setalias.setIcon(QtGui.QIcon.fromTheme('user-properties'))
        
        self.ui.alias_button.setIcon(QtGui.QIcon.fromTheme('document-save'))
        #self.ui..setIcon(QtGui.QIcon.fromTheme(''))
        #self.ui..setIcon(QtGui.QIcon.fromTheme(''))
        #self.ui..setIcon(QtGui.QIcon.fromTheme(''))
        #self.ui..setIcon(QtGui.QIcon.fromTheme(''))
        #self.ui..setIcon(QtGui.QIcon.fromTheme(''))
        #self.ui..setIcon(QtGui.QIcon.fromTheme(''))
        #self.ui..setIcon(QtGui.QIcon.fromTheme(''))
        
        self.show_friend_from_item(self.ui.friendsList.item(0), None)
        
        self.connect(self.ui.colectionTree,
                     QtCore.SIGNAL('customContextMenuRequested(const QPoint &)'),
                     self.showColectionTreeMenu)
                     
                     
        self.connect(self.ui.friendsList,
                     QtCore.SIGNAL('customContextMenuRequested(const QPoint &)'),
                     self.show_friends_list_menu
                     )
                     
                     
        self.connect(self.ui.colectionTree,
                     QtCore.SIGNAL('currentItemChanged(QTreeWidgetItem *,QTreeWidgetItem *)'),
                     self.show_item
                     )
                     
                     
        self.connect(self.ui.friendsList,
                     QtCore.SIGNAL('currentItemChanged(QListWidgetItem *,QListWidgetItem *)'),
                     self.show_friend_from_item
                     )
                     
                     
        self.connect(self.ui.alias_button,
                     QtCore.SIGNAL('clicked()'),
                     self.set_alias
                     )
                     
        self.connect(self.ui.author_identicon,
                     QtCore.SIGNAL('clicked()'),
                     self.show_friend_from_id
                     )
                     
                     
                     
        #self.connect(self.ui.friendsList,
                     #QtCore.SIGNAL('itemDoubleClicked(QListWidgetItem*,int)'),
                     #self.show_friend_from_item)


        
        
        self.connect(self.ui.action_file_read,
                     QtCore.SIGNAL('triggered()'),
                     self.read_file
                    )
        self.connect(self.ui.action_file_import,
                     QtCore.SIGNAL('triggered()'),
                     self.import_file
                    )
        self.connect(self.ui.action_file_export,
                     QtCore.SIGNAL('triggered()'),
                     self.export_file
                    )
        self.connect(self.ui.actionLock_panels,
                     QtCore.SIGNAL('toggled(bool)'),
                     self.lock_dock
                    )
                    
        self.connect(self.ui.action_contextualfriend_share_external,
                     QtCore.SIGNAL('triggered()'),
                     self.friend_share
                    )
        self.connect(self.ui.action_contextualfriend_add,
                     QtCore.SIGNAL('triggered()'),
                     self.friend_add
                    )
        self.connect(self.ui.action_contextualfriend_remove,
                     QtCore.SIGNAL('triggered()'),
                     self.friend_remove
                    )
        self.connect(self.ui.action_contextualfriend_show,
                     QtCore.SIGNAL('triggered()'),
                     self.show_friend_from_none
                    )
                    
                    
        self.connect(self.ui.colection,
                     QtCore.SIGNAL('currentIndexChanged(QString)'),
                     self.update_file
                    )
                    
                    
                    
        self.show()
        
        
    def update_file(self, colection):
        self.ui.file.clear()
        self.ui.file.addItems(FILES[str(colection)])
        
        
    def friend_share(self):
        item=self.ui.friendsList.currentItem()
        print('share with '+item.text())
        
        
    def friend_add(self):
        item=self.ui.friendsList.currentItem()
        print('share with '+item.text())
        
        
    def friend_remove(self):
        item = self.ui.friendsList.currentItem()
        print(os.path.join(FRIENDS_PATH,str(item.text())))
        os.remove(os.path.join(FRIENDS_PATH,str(item.text())))
        load_global_friends()
        self.friend_list_update()
        
    def colection_tree_update(self):
        self.ui.colectionTree.clear()
        for colection in FILES.keys():
            colection_item = QtGui.QTreeWidgetItem()
            colection_item.setText(0,colection)
            colection_item.setIcon(0,QtGui.QIcon.fromTheme('folder'))
            for file in FILES[colection]:
                file_item = QtGui.QTreeWidgetItem()
                file_item.setText(0,file)
                file_item.setIcon(0,QtGui.QIcon(os.path.join(COLECTION_PATH,
                                                             colection,file)))
                colection_item.addChild(file_item)
                    
            self.ui.colectionTree.addTopLevelItem(colection_item)
        
        
    def friend_list_update(self):
        #self.ui.friendsList.clear()
        self.ui.friendsList.clear()
        for friend in FRIENDS:
            friend_item = QtGui.QListWidgetItem()
            friend_item.setText(get_friend_displayname(friend))
            friend_item.setIcon(QtGui.QIcon(get_identicon_24_pixmap(friend)))
            friend_item.setStatusTip(str(friend))
                    
            self.ui.friendsList.addItem(friend_item)
        
        
    def show_friends_list_menu(self, pos):
        self.ui.friend_menu.popup(QtGui.QCursor(pos).pos())
                
            
    def show_friend_from_item(self, current_item, previous_item):
        self.user_id = str(current_item.statusTip())
        self.user_alias = FRIENDS[self.user_id][0]
        self.show_friend()
        
    def show_friend_from_none(self):
        self.user_id = str(self.ui.friendsList.currentItem().statusTip())
        self.user_alias = FRIENDS[self.user_id][0]
        self.show_friend()
        
        
    def show_friend_from_id(self):
        self.user_id = str(self.ui.author.text())
        try:
            self.user_alias = FRIENDS[self.user_id]
            self.show_friend()
        except KeyError:
            print(self.user_id + ' is not in your friends')
        
        
    def show_friend(self):
        self.ui.friend_name.setText(get_friend_displayname(self.user_id))
        self.ui.user_id.setText(self.user_id)
        self.ui.alias.setText(self.user_alias)
        self.ui.identicon.setPixmap(get_identicon_pixmap(self.user_id))
        self.ui.main_stacked.setCurrentIndex(1)
        
        
    def set_alias(self):
        print('Launched set_alias')
        friend_file_name = self.user_id + self.user_alias
        new_friend_file_name = self.user_id + str(self.ui.alias.text())
        print((os.path.join(FRIENDS_PATH,friend_file_name), os.path.join(FRIENDS_PATH,new_friend_file_name)))
        os.rename(os.path.join(FRIENDS_PATH,friend_file_name), os.path.join(FRIENDS_PATH,new_friend_file_name))
        
        update_global_friend_alias(self.user_id,str(self.ui.alias.text()))
        
        self.user_alias = str(self.ui.alias.text())
        if self.user_alias == '':
            self.user_alias = self.user_id
        
        self.ui.friendsList.currentItem().setText(self.user_alias)

        
    def showColectionTreeMenu(self, pos):
        
        index = self.ui.colectionTree.indexAt(pos)
        
        if index.parent().isValid():
            self.ui.file_menu.popup(QtGui.QCursor(pos).pos())
        else:
            self.ui.colection_menu.popup(QtGui.QCursor(pos).pos())

    def show_item(self, current_item, previous_item):
        parent = current_item.parent()
        if parent:
            self.ui.main_stacked.setCurrentIndex(0)
            self.ui.colection.setCurrentIndex(FILES.keys().index(parent.text(0)))
            self.ui.file.setCurrentIndex(FILES[str(parent.text(0))].index(current_item.text(0)))
            
            file_handler = open(os.path.join(COLECTION_PATH,str(parent.text(0)),str(current_item.text(0))))
            file_header = extract_file_header(file_handler)
            self.ui.keylength.setValue(file_header['aes_key_length'])
            self.ui.author.setText(file_header['author'])
            self.ui.author_identicon.setIcon(QtGui.QIcon(get_identicon_24_pixmap(file_header['author'])))
            
            if file_header['input_date']:
                self.ui.systemimputdate.setDateTime(QtCore.QDateTime(1970,1,1,1,0).addSecs(file_header['input_date']))
                #self.ui.systemimputdate.setDisplayFormat('d MMM yyyy HH:mm:ss')
            else:
                self.ui.systemimputdate.clear()
                self.ui.systemimputdate.setEnabled(False)
                #self.ui.systemimputdate.setDisplayFormat('z')
                
            if file_header['share_date']:
                #self.ui.sharedate.setDisplayFormat('d MMM yyyy HH:mm:ss::')
                self.ui.sharedate.setDateTime(QtCore.QDateTime(1970,1,1,1,0).addSecs(file_header['share_date']))
            else:
                self.ui.sharedate.clear()
                self.ui.sharedate.setEnabled(False)
                #self.ui.sharedate.setDisplayFormat('z')
                
            if file_header['import_date']:
                #self.ui.importdate.setDisplayFormat('d MMM yyyy HH:mm:ss')
                self.ui.importdate.setDateTime(QtCore.QDateTime(1970,1,1,1,0).addSecs(file_header['import_date']))
            else:
                self.ui.importdate.clear()
                self.ui.importdate.setEnabled(False)
        
            
    def lock_dock(self, locked):
        if locked:
            self.ui.colectionsDock.setFeatures(QtGui.QDockWidget.DockWidgetFeatures(0))
            self.ui.friendsDock.setFeatures(QtGui.QDockWidget.DockWidgetFeatures(0))
        else:
            self.ui.colectionsDock.setFeatures(QtGui.QDockWidget.DockWidgetFeatures(7))
            self.ui.friendsDock.setFeatures(QtGui.QDockWidget.DockWidgetFeatures(7))


    def read_file( self ):
        input_file = open(self.choose_file('Open file', ''), 'r')


    def import_file( self ):
        import_dialog = ImportDialog(self)
        import_dialog.exec_()
        load_global_files()
        self.colection_tree_update()


    def export_file( self ):
        export_dialog = ExportDialog(self)
        export_dialog.show()


    def choose_colection(self, dialogTitle, inputText):
        dialog = QtGui.QInputDialog
        colection, ok = dialog.getItem(self, dialogTitle, inputText, FILES.keys(), 0, False)
        
        if ok:
            return os.path.join(COLECTION_PATH, str(colection))
    
    
    def choose_colection_file(self, dialogTitleC, inputTextC, dialogTitleF, inputTextF):
        colection = self.choose_colection(dialogTitleC, inputTextC)
        
        if colection:
            files = []
            for file in os.listdir(os.path.join(colection)):
                if not os.path.isdir(os.path.join(colection,file)):
                    files.append(file)
                    
        dialog = QtGui.QInputDialog
        file, ok = dialog.getItem(self, dialogTitleF, inputTextF, files, 0, False)
        
        if ok:
            return os.path.join(colection, str(file))


    #def load_rsakey(self):
        #while not os.path.exists(RSAKEY_PATH):
            #new_rsa_dialog = NewRsaDialog(self)
            #new_rsa_dialog.exec_()
        
        #key_file = open(RSAKEY_PATH, 'r')
        
        #rsakey = RSA.importKey(key_file.read())
        
        #key_id = get_rsakey_id(rsakey)
        
        #key_identicon = get_identicon_pixmap(key_id)
        
        #key_identicon_24 = key_identicon.scaled(24, 24, 1, 1)
        
        #load_global_rsakey_data(rsakey, key_id, key_identicon, key_identicon_24)
        
    #def load_rsakey(self):
        ##self.get_rsakey()
            #self.get_rsakey()
            
    
    
    
            
    def load_program(self):
        pixmap = QtGui.QPixmap(IMAGES_PATH + '/flashscreen.png')
        
        splash = QtGui.QSplashScreen(pixmap)
        progressBar = QtGui.QProgressBar(splash)
        progressBar.setGeometry(splash.width()/10, 8*splash.height()/10,
                                8*splash.width()/10, splash.height()/10)
        splash.show()
        
        progressBar.setValue(0)
        
        progressBar.setFormat('Loading global files')
        print('Loading global files')
        load_global_files()
        progressBar.setValue(20)
        
        progressBar.setFormat('Loading global friends')
        print('Loading global friends')
        load_global_friends()
        progressBar.setValue(40)
        
        progressBar.setFormat('Getting RSA key')
        print('Getting RSA key')
        load_rsakey(self)
        progressBar.setValue(60)
        
        progressBar.setFormat('Loading GUI (Colection tree)')
        self.colection_tree_update()
        progressBar.setValue(80)
        
        progressBar.setFormat('Loading GUI (Friends list)')
        self.friend_list_update()
        progressBar.setValue(100)
    
            

#class NewRsaDialog(QtGui.QDialog):
    #def __init__(self, parent):
        #QtGui.QDialog.__init__(self, parent)
        
        #self.ui = Ui_NewRsaDialog()
        #self.ui.setupUi(self)
        
        #self.rsakey = None
        #self.progress_dialog = None
        ##for i in (1024,2048,4096,8192,16384,32768):
            ##print(i)
            ##self.st = time.time()
            ##key_ = generate_rsakey(i)
            ##self.et = time.time()
            ##print('generate: '+ str(self.et-self.st))
            ##self.st = time.time()
            ##import_encrypt_file('a','b',key_,32)
            ##self.et = time.time()
            ##print('encrypt:  '+ str(self.et-self.st))
                
        ##self.connect(self.ui.newrsakeyr,
                     ##QtCore.SIGNAL('toggled(bool)'),
                     ##self.key_getter_update
                    ##)
                
        #self.connect(self.ui.newrsakey,
                     #QtCore.SIGNAL('valueChanged(int)'),
                     #self.new_rsakey_length_update
                    #)
                    
        #self.connect(self.ui.buttonBox,
                     #QtCore.SIGNAL('accepted()'),
                     #self.accepted
                    #)
                    
        #self.connect(self.ui.action,
                     #QtCore.SIGNAL('clicked()'),
                     #self.action
                    #)
                    
    ##def key_getter_update(self, value):
        ##print('Update key features')
        ##if self.ui.newrsakeyr.isChecked():
            ##self.ui.security.setValue(10000-5120000/self.ui.newrsakey.value())
            ##self.ui.action.setText('Create')
        ##elif self.ui.fromfiler.isChecked():
            ##self.ui.action.setText('Import')
            ##self.ui.security.setValue(0)
        ##else:
            ##print('WTF')
            
            
    #def action(self):
            
        ##self.progress_dialog = QtGui.QProgressDialog('Key generation','Cancel',0,6,self)
        #self.progress_dialog = QtGui.QProgressDialog(self)
        #self.progress_dialog.setRange(0,6)
        
        #def increment_progress(s,increment=1,process='Generating RSA key'):
            #print(str(self.progress_dialog.labelText()),self.progress_dialog.value(),increment)
            #self.progress_dialog.setValue(self.progress_dialog.value() + increment)
            
            ##self.progress_dialog.setFormat(process)
        ##self.progress_dialog = QtGui.QProgressDialog()
        ##self.progress_dialog.setMinimum(0)
        ##self.progress_dialog.setMaximum(6)
        ##self.progress_dialog.setValue(-1) # As set in Designer
        
        #increment_progress('',0,'Creating random generator')
        #self.ui.action.setEnabled(False)
        #if self.ui.newrsakeyr.isChecked():
            #increment_progress('',1,'Generating RSA key')
            #random_generator = Random.new().read
            #increment_progress('')
            #self.rsakey =  RSA.generate(self.ui.newrsakey.value(), random_generator,increment_progress)
        #elif self.ui.fromfiler.isChecked():
            #print('not available')
            #self.rsakey = None
        #else:
            #print('WTF')
            #self.rsakey = None
            
        
        #increment_progress('',1,'Creating key identificator')
        #key_id = get_rsakey_id(self.rsakey)
        #self.ui.keyid.setText(key_id)
        #increment_progress('',1,'Creating key identicon')
        #create_identicon(key_id)
        #increment_progress('',0,'New key created')
        
        #pixmap = get_identicon_pixmap(key_id).scaled (24, 24, 1, 1)
        
        #self.ui.author_identicon.setPixmap(pixmap)
        #self.ui.action.setEnabled(True)
        
        
   
                    
    #def new_rsakey_length_update(self, value):
        #self.ui.security.setValue(10000-5120000/self.ui.newrsakey.value())
    
    
    #def accepted(self):
        #return 'ok'
            

class ImportDialog(QtGui.QDialog):
    def __init__(self, parent):
        QtGui.QDialog.__init__(self, parent)
        
        self.ui = Ui_ImportDialog()
        self.ui.setupUi(self)
        
        self.ui.colectionCombobox.addItems(FILES.keys())
        
        self.connect(self.ui.importfileToolbutton,
                     QtCore.SIGNAL('clicked()'),
                     self.select_import_file
                    )
                    
        self.connect(self.ui.buttonBox,
                     QtCore.SIGNAL('accepted()'),
                     self.import_file
                    )
                    
    def select_import_file(self):
        input_file_path = choose_file(self, 'Import file', '')
        self.ui.importfileLineedit.setText(input_file_path)
        self.ui.filenameLineedit.setText(os.path.basename(input_file_path))
    
    
    def import_file(self):
        input_file_path = str(self.ui.importfileLineedit.text())
        output_file_path = os.path.join(COLECTION_PATH,
                                        str(self.ui.colectionCombobox.currentText()),
                                        str(self.ui.filenameLineedit.text())
                                       )
        key_length = self.ui.keylengthSpinbox.value()
        import_file(input_file_path, output_file_path, key_length)
            

class ExportDialog(QtGui.QDialog):
    def __init__(self, parent):
        QtGui.QDialog.__init__(self, parent)
        
        self.ui = Ui_ExportDialog()
        self.ui.setupUi(self)
        
        self.ui.colectionCombobox.addItems(FILES.keys())
        
        self.colection_update(FILES.keys()[0])
        
        self.connect(self.ui.importfileToolbutton,
                     QtCore.SIGNAL('clicked()'),
                     self.select_export_file
                    )
                    
        self.connect(self.ui.buttonBox,
                     QtCore.SIGNAL('accepted()'),
                     self.export_file
                    )
                    
        self.connect(self.ui.colectionCombobox,
                     QtCore.SIGNAL('currentIndexChanged(QString)'),
                     self.colection_update
                    )


    def colection_update(self, colection):
        self.ui.filenameCombobox.clear()
        self.ui.filenameCombobox.addItems(FILES[str(colection)])
    
    
    def select_export_file(self):
        input_file_path = choose_file(self, 'Import file', '')
        self.ui.exportfileLineedit.setText(input_file_path)
    
    
    def export_file(self):
        input_file_path = os.path.join(COLECTION_PATH,
                                       str(self.ui.colectionCombobox.currentText()),
                                       str(self.ui.filenameCombobox.currentText())
                                      )
        output_file_path = str(self.ui.exportfileLineedit.text())
        
        export_file(input_file_path, output_file_path)


def import_file(input_file_path, output_file_path, key_length):
    import_encrypt_file(input_file_path, output_file_path, RSAKEY, key_length)
    print('Encrypt finished')
    load_global_files()
    
    
def export_file(input_file_path, output_file_path):
    export_decrypt_file(input_file_path, output_file_path, RSAKEY)
    print('Decrypt finished')
    load_global_files()
    


def choose_file(parent, dialogTitle, defaultPath):
    fileName = QtGui.QFileDialog.getOpenFileName(parent, dialogTitle, 
                                                    defaultPath)
    return str(fileName)

def create_rsakey_file(rsakey):
    rsakey_file = open(RSAKEY_PATH, 'w')
    rsakey_file.write(rsakey.exportKey('PEM'))
    rsakey_file.close()
    
    
def load_rsakey_file():
    rsakey_file = open(RSAKEY_PATH, 'r')
    global RSAKEY
    RSAKEY = RSA.importKey(rsakey_file.read())
    global KEY_ID
    KEY_ID = get_rsakey_id(RSAKEY)
    global KEY_IDENTICON
    KEY_IDENTICON = get_identicon_pixmap(KEY_ID)
    global KEY_IDENTICON_24
    KEY_IDENTICON_24 = get_identicon_24_pixmap(KEY_ID)
    rsakey_file.close()
    
    
def load_rsakey(parent):
    


    def throw_get_rsakey_dialog():
        pixmap = QtGui.QIcon.fromTheme('preferences-desktop-cryptography').pixmap(QtCore.QSize(128,128))
        get_rsakey_dialog = QtGui.QDialog(parent)
        get_rsakey_dialog.ui = Ui_GetRsaDialog()
        get_rsakey_dialog.ui.setupUi(get_rsakey_dialog)
        get_rsakey_dialog.ui.icon.setPixmap(pixmap)
        if get_rsakey_dialog.exec_():
            if get_rsakey_dialog.ui.newrsakeyr.isChecked():
                throw_get_rsakey_dialog_create()
        else:
            print('imp')


    def throw_get_rsakey_dialog_create(default_length=2048):
        icon = QtGui.QIcon.fromTheme('preferences-desktop-cryptography').pixmap(QtCore.QSize(128,128))
        
        
        def new_rsakey_length_update(value):
            get_rsakey_dialog_create.ui.security.setValue(10000-5120000/value)
            get_rsakey_dialog_create.ui.keylength_slide.setValue(value/256)
            
            
        def new_rsakey_length_slide_update(value):
            get_rsakey_dialog_create.ui.keylength.setValue(value*256)
        
            
         
            
            
        
        
        get_rsakey_dialog_create = QtGui.QDialog(parent)
        get_rsakey_dialog_create.ui = Ui_GetRsaDialogCreate()
        get_rsakey_dialog_create.ui.setupUi(get_rsakey_dialog_create)
        get_rsakey_dialog_create.ui.icon.setPixmap(icon)
        
        get_rsakey_dialog_create.connect(get_rsakey_dialog_create.ui.keylength,
                                        QtCore.SIGNAL('valueChanged(int)'),
                                        new_rsakey_length_update
                                        )
        
        get_rsakey_dialog_create.connect(get_rsakey_dialog_create.ui.keylength_slide,
                                        QtCore.SIGNAL('valueChanged(int)'),
                                        new_rsakey_length_slide_update
                                        )
                                        
        get_rsakey_dialog_create.ui.keylength.setValue(default_length)
                                        
                                        
        
        if get_rsakey_dialog_create.exec_():
            key_length = get_rsakey_dialog_create.ui.keylength.value()
            if key_length > 8192:
                get_rsakey_dialog_keylengthalert = QtGui.QMessageBox(QtGui.QMessageBox.Warning,'The key length is too big', 'The key length is bigger then 8192, it could take so much time to generate it. Are you sure you want to generate a ' + str(key_length) + ' bytes key?', QtGui.QMessageBox.Yes, parent)
                get_rsakey_dialog_keylengthalert.addButton(QtGui.QMessageBox.No)
                if get_rsakey_dialog_keylengthalert.exec_() == 16384:
                    create_key(key_length)
                else:
                    throw_get_rsakey_dialog_create(key_length)
            else:
                create_key(key_length)


    def create_key(key_length):
        def add(s):
            get_rsakey_dialog_progress.setValue(get_rsakey_dialog_progress.value()+1)
        
        
        get_rsakey_dialog_progress = QtGui.QProgressDialog(parent)
        get_rsakey_dialog_progress.setMaximum(5)
        get_rsakey_dialog_progress.show()
        get_rsakey_dialog_progress.setAutoClose(True)
        
        get_rsakey_dialog_progress.setLabelText('Generating random seed')
        random_generator = Random.new().read
        get_rsakey_dialog_progress.setValue(get_rsakey_dialog_progress.value()+1)
        
        get_rsakey_dialog_progress.setLabelText('Generating RSA key')        
        rsakey =  RSA.generate(key_length, random_generator,add)
        
        get_rsakey_dialog_progress.setLabelText('Generating key id')
        key_id = get_rsakey_id(rsakey)
        get_rsakey_dialog_progress.setValue(get_rsakey_dialog_progress.value()+1)
        
        get_rsakey_dialog_progress.setLabelText('Adding identicon')
        create_identicon(key_id)
        identicon = get_identicon_24_pixmap(key_id)
        get_rsakey_dialog_progress.setValue(get_rsakey_dialog_progress.value()+1)
        throw_get_rsakey_dialog_result(rsakey, key_id, identicon, key_length)


    def throw_get_rsakey_dialog_result(rsakey, key_id, identicon, key_length):
        def clic(button):
            button_text = button.text()
            if button_text == 'Save':
                create_rsakey_file(rsakey)
            elif button_text == 'Retry':
                get_rsakey_dialog_result.accept()
                create_key(key_length)
            elif button_text == 'Discard':
                get_rsakey_dialog_result.reject()
                
                
        def show():
            throw_get_rsakey_dialog_show(get_rsakey_dialog_result, rsakey)
                
                
        icon = QtGui.QIcon.fromTheme('preferences-desktop-cryptography').pixmap(QtCore.QSize(128,128))
        
        get_rsakey_dialog_result = QtGui.QDialog(parent)
        get_rsakey_dialog_result.ui = Ui_GetRsaDialogResult()
        get_rsakey_dialog_result.ui.setupUi(get_rsakey_dialog_result)
        get_rsakey_dialog_result.ui.key_id.setText(key_id)
        #get_rsakey_dialog_result.ui.key_pem.setText(rsakey.exportKey('PEM'))
        get_rsakey_dialog_result.ui.key_identicon.setPixmap(identicon)
        get_rsakey_dialog_result.ui.icon.setPixmap(icon)
        get_rsakey_dialog_result.connect(get_rsakey_dialog_result.ui.buttonBox,
                                         QtCore.SIGNAL('clicked(QAbstractButton *)'),
                                         clic);
        get_rsakey_dialog_result.connect(get_rsakey_dialog_result.ui.rsakey_show,
                                         QtCore.SIGNAL('clicked()'),
                                         show);
        get_rsakey_dialog_result.exec_()


    def throw_get_rsakey_dialog_show(parent, rsakey):
        get_rsakey_dialog_show = QtGui.QDialog(parent)
        get_rsakey_dialog_show.ui = Ui_GetRsaDialogShow()
        get_rsakey_dialog_show.ui.setupUi(get_rsakey_dialog_show)
        
        get_rsakey_dialog_show.ui.key_pem.setText(rsakey.exportKey('PEM'))
        
        get_rsakey_dialog_show.exec_()


    if not os.path.exists(RSAKEY_PATH):
        throw_get_rsakey_dialog()
    
    if os.path.exists(RSAKEY_PATH):
        load_rsakey_file()
#def get_rsakey():
    #if os.path.exists(RSAKEY_PATH):
        #key_file = open(RSAKEY_PATH, 'r')
        #return RSA.importKey(key_file.read())
    #else:
        #return None



    
#def add_file():
    #continue


if __name__ == '__main__':
    #for i in range(0,100):
        #_rsa = generate_rsakey(1024)
        #create_rsapub_file(get_rsakey_id(_rsa) ,_rsa)
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())