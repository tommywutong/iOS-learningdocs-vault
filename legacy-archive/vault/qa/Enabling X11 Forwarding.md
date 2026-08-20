---
title: Enabling X11 Forwarding
apple_id: DTS10003415
resource_type: QA
platform: macOS
topic: Cross Platform
technology: null
published: '2004-10-25'
source_url: https://developer.apple.com/library/archive/qa/qa1383/_index.html
archived_at: '2026-07-18T02:30:29.344205Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1383

# Enabling X11 Forwarding

## Q:  I need to ssh to a remote Mac OS X system and run an X11 application. However, when I try to execute the application, the system responds with "Error: Can't open display: ". What's wrong?

A: The remote system does not have "X11 forwarding" enabled. X11 forwarding allows the X11 connection to be tunneled from the remote system to the local system. For security reasons, Mac OS X does not enable X11 forwarding by default. In order for clients to receive X11 forwarding, the system administrator must explicitly enable it on the Mac OS X system. This is done by altering the /etc/sshd_config file, either by manual edit, or as shown in Listing 1.

__Listing 1__  Enabling X11 Forwarding

```
sed 's/#X11Forwarding\ no/X11Forwarding\ yes/' /etc/sshd_config > /tmp/sshd_config
sudo mv /tmp/sshd_config /etc/.
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-10-25 | Updated command line syntax. |
| 2004-09-23 | New document that describes how to enable ssh clients to receive X11 communication from a Mac OS X system. |

