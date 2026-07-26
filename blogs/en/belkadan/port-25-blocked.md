---
title: Port 25 Blocked?
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2007/07/Port-25-Blocked/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:0655371f3a00633b'
translated: false
---

> 原文：[Port 25 Blocked?](https://belkadan.com/blog/2007/07/Port-25-Blocked/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [GenericToolbar Icon](https://belkadan.com/blog/2007/06/GenericToolbar-Icon/)

[Short Xcode Tip: Plugins](https://belkadan.com/blog/2007/09/Short-Xcode-Tip-on-Plugins/) »

[HTTPS and Name-based Virtual Hosting](https://belkadan.com/blog/2008/08/HTTPS-and-Name-based-Virtual-Hosting/?tag=unix) »

## [Port 25 Blocked?](#)

**Warning! Linux jargon ahead!**

My Internet just recently switched to AT&T U-verse, and I’m not hugely impressed one way or the other. It feels a bit more glitchy than before, but maybe that’s just the AT&T-provided wireless router. I don’t really know. (Is anyone having problems viewing this site? Not that there are that many people viewing the site at all.)

But the part I was most worried about was the fact that outgoing traffic on port 25 was blocked.

Port 25, for those of you who don’t know, is the TCP port used to transfer e-mail. There _is_ the possibility of using the lesser-known port 587 (the “submission” port). The trouble is that this sort of defeats the purpose of having a separate submission port. In any case, I didn’t want to try to figure out how to set up traffic to leave from port 587 on my server and come out at port 25 on the recipient’s. (My server, by the way, is an old PC running Debian Linux, not the Mac I use for programming.)

But there was another solution, one that’s been built into most mail transfer agents since the beginning. Relay hosts.

Basically, AT&T knows that most people don’t have e-mail servers sitting around in their houses, and yet there are plenty of people who want to send and receive e-mail at home, using a client like Microsoft Outlook or Apple Mail. (Clearly these people are not Webmailer users.) So what do they do? They provide their own e-mail servers. The SMTP server they have takes e-mail from a desktop client and forwards it out to its proper destination.

Hey, that’s exactly what I need! By logging into the AT&T account, you can find your SMTP server. I’ll give you AT&T’s here, but if you have another provider you’ll have to find the equivalent server on your own: `smtp.att.yahoo.com`

Next we do a bit of digging in the mail transfer agent’s configuration. I’m using Postfix, but the concepts apply to other MTAs like Exim4 or Qmail. For whatever reason, AT&T restricts use of their SMTP servers to people with valid AT&T accounts, so we’ve got an extra hurdle to jump: authentication. You have to update your MTA’s main configuration file; the changes in my Postfix `main.cf` file looked like this:

```
# The brackets [] say that this is an SMTP server and not to use DNS
# to lookup, via MX record, where the SMTP server actually lives
relayhost = [smtp.att.yahoo.com]

# Authentication
smtp_sasl_auth_enable = yes
smtp_sasl_password_maps = hash:/etc/postfix/sasl/passwd
# You can set this to noanonymous if you want
smtp_sasl_security_options =
```

OK, so far so good. Note that you do need to have SASL installed for this to work. If not, you can issue a quick `apt-get postfix-tls libsasl2-modules` as root to fix that. (At least on Debian.)

Finally, we have to make that file, `/etc/postfix/sasl/passwd`. This is a really simple file of the form `smtp.att.yahoo.com user@att.net:password`, with one server per line. Of course, you have to use your own att.net (or sbcglobal.net, or whatever) username and password. Once that’s done you’ll want to make the file owned by root and not readable by anyone else, since it has a plaintext password in there: `chown root:root /etc/postfix/sasl/passwd; chmod 600 /etc/postfix/sasl/passwd`. Finally, put it in a form that’s readable by Postfix: `postmap /etc/postfix/sasl/passwd`.

Reload Postfix, or whatever MTA you have, now that you’ve set up authentication and specified a relay host. Try to send mail.

So, if you don’t receive the mail you sent to yourself (and that’s usually a good test if you also have a Yahoo or Gmail account) you’ve come across the one little problem. Because you’re now using a _shared_ server, it seems to send e-mail in batches. When those batches go out, you can’t be sure. Bummer!

Still, the solution works, and port 25 is still blocked. I’ve been told, however, that the U-verse tech support people are willing to unblock it for you. Perhaps I’ll see if that’s true some day.

This entry was posted on [July](https://belkadan.com/blog/2007/07) 15, [2007](https://belkadan.com/blog/2007) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Unix](https://belkadan.com/blog/tags/unix)
