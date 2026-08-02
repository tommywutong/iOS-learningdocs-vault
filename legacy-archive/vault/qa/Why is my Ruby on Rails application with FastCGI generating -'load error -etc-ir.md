---
title: Why is my Ruby on Rails application with FastCGI generating "'load error /etc/irbrc"
  errors?
apple_id: DTS10004504
resource_type: QA
platform: macOS
topic: Cross Platform
technology: null
published: '2007-11-28'
source_url: https://developer.apple.com/library/archive/qa/qa1494/_index.html
archived_at: '2026-07-18T02:31:30.696018Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1494

# Why is my Ruby on Rails application with FastCGI generating "'load error /etc/irbrc" errors?

## Q:  Why is my Ruby on Rails application with FastCGI generating "load error /etc/irbrc" errors?

A: Why is my Ruby on Rails application with FastCGI generating "load error /etc/irbrc" errors?

If you're hosting Ruby on Rails applications on Mac OS X 10.5 or Mac OS X 10.5 Server with FastCGI, you may encounter an error when accessing your application, accompanied by an error in the Apache error log, similar to the message in Listing 1 :

__Listing 1__  Sample Apache error log message from FastCGI.

```
[error] [client ::1] FastCGI: comm with server "/Library/WebServer/Documents/demoapp/dispatch.fcgi" aborted:  error parsing headers: malformed header 'load error /etc/irbrc'
```

To resolve this, first back up your current `/etc/irbrc` file and then replace it with the contents of Listing 2 (this requires admin privileges), and then restart your web server.

__Listing 2__  Replace your /etc/irbc file with these lines.

```
require 'irb/completion' require 'irb/ext/save-history' ARGV.concat [ "--readline", "--prompt-mode", "simple" ] IRB.conf[:SAVE_HISTORY] = 100 IRB.conf[:HISTORY_FILE] = "#{ENV['HOME']}/.irb-save-history"
```

Here is one way of doing this from within Terminal:

Make a backup of `/etc/irbrc`


```
% sudo mv /etc/irbrc /etc/irbc.orig
```

Create and edit a new, empty copy of `/etc/irbrc`


```
% sudo pico /etc/irbrc
```

Copy Listing 2 and paste it into the new document, then save the file by pressing, in order, "Control-X" (Exit), "Y" (Yes), and "Return".

Change the permissions of `/etc/irbrc` to match the original (Read-only for User, Group and Others)


```
% sudo chmod a=r /etc/irbrc
```

Finally, restart Apache


```
% sudo apachectl graceful
```

Internal: <rdar://problem/5517579>

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-11-28 | New document that describes how to resolve an error encountered hosting Ruby on Rails applications on Mac OS X 10.5. |

