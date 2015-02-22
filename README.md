# AK-FS

Asymmetric Key File Sharer is an application that intends to simplify and become humanly friendly using asymmetric encryption file sharing.

## **DO NOT USE**

This application **is not safe**, it is in development, it is not usable.

## Bugs

### General
* When there is no friend, the application crashes:
```
Traceback (most recent call last):
  File "__init__.py", line 1105, in <module>
    main = MainWindow()
  File "__init__.py", line 374, in __init__
    self.show_friend_from_item(self.ui.friendsList.item(0), None)
  File "__init__.py", line 518, in show_friend_from_item
    self.user_id = str(current_item.statusTip())
AttributeError: 'NoneType' object has no attribute 'statusTip'
```

### GUI


## ToDo

### Security
* Improve the identicons system. Is now easy to impersonate a identicon.
* Encrypt the private key with a start password.

### GUI
* Contextual menus in the GUI.
* Clean identicon.py module.
