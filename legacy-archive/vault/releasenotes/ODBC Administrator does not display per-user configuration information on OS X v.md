---
title: ODBC Administrator does not display per-user configuration information on OS
  X v10.6
apple_id: TP40009078
resource_type: Release Note
platform: macOS
topic: Languages & Utilities
technology: null
published: '2009-09-02'
source_url: https://developer.apple.com/library/archive/releasenotes/ToolsLanguages/ODBCNoPerUserConfigs106/_index.html
archived_at: '2026-07-18T02:59:02.479708Z'
---
> 导航：[总目录](../README.md) · [releasenotes](../_indexes/releasenotes.md)



## ODBC Administrator does not display per-user configuration information on Mac OS X v10.6

### Problem Description

The version of `iodbc` shipped on OS X was upgraded to 2.52.6 in Mac OS X v10.6. The new version expects to find user-specific configuration information at `~/.odbc.ini` and `~/.odbcinst.ini` instead of `~/Library/ODBC/odbc.ini` and `~/Library/ODBC/odbcinst.ini` where previous versions placed it.

There are two issues that result from this change:

- `iodbc` does not find existing configuration information, and may not find newly-created configuration information created by the ODBC Administrator tool.
- ODBC Administrator (downloadable from [http://support.apple.com/](http://support.apple.com/)) does not find existing configuration information, and may not find newly-created configuration information.

### Workaround

To work around the problem, you can create a symbolic link between each pair of locations in one of the following two ways.

#### For existing users who have already configured user DSNs

While logged in as the existing user, launch Terminal.

In Terminal, enter the following commands :

```
ln -s Library/ODBC/odbc.ini .odbc.ini
ln -s Library/ODBC/odbcinst.ini .odbcinst.ini
```


#### For new users who do not yet have configured user DSNs

While logged in as the new user, launch Terminal.

In Terminal, enter the following commands :

```
mkdir -p Library/ODBC
touch Library/ODBC/odbc.ini
touch Library/ODBC/odbcinst.ini
ln -s Library/ODBC/odbc.ini .odbc.ini
ln -s Library/ODBC/odbcinst.ini .odbcinst.ini
```


