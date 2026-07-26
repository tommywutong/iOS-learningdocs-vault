---
title: HTTPS and Name-based Virtual Hosting
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2008/08/HTTPS-and-Name-based-Virtual-Hosting/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:948f171e58614f3d'
translated: false
---

> 原文：[HTTPS and Name-based Virtual Hosting](https://belkadan.com/blog/2008/08/HTTPS-and-Name-based-Virtual-Hosting/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Alerts Without Apps (or nibs)](https://belkadan.com/blog/2008/03/Alerts-Without-Apps/)

[Objective-J and Objective-C](https://belkadan.com/blog/2008/09/Objective-J-and-Objective-C/) »

[Setting up gitweb on Shared Hosting](https://belkadan.com/blog/2020/01/Gitweb-on-Shared-Hosting/?tag=apache) »

« [Port 25 Blocked?](https://belkadan.com/blog/2007/07/Port-25-Blocked/?tag=unix)

[Z shell](https://belkadan.com/blog/2009/06/Z-shell/?tag=unix) »

## [HTTPS and Name-based Virtual Hosting](#)

If you’ve been running your own server for a while, eventually you’ll start getting privacy jitters and want to use HTTPS, at which point you’ll either happily set it up with minimal difficulty (if you’re running a single site) or realize frustratedly that you can’t use HTTPS with name-based virtual hosts. To quote the Apache site:

> The reason is very technical, and a somewhat “chicken and egg” problem. The SSL protocol layer stays below the HTTP protocol layer and encapsulates HTTP. When an SSL connection (HTTPS) is established Apache/mod_ssl has to negotiate the SSL protocol parameters with the client. For this, mod_ssl has to consult the configuration of the virtual server (for instance it has to look for the cipher suite, the server certificate, etc.). But in order to go to the correct virtual server Apache has to know the Host HTTP header field. To do this, the HTTP request header has to be read. This cannot be done before the SSL handshake is finished, but the information is needed in order to complete the SSL handshake phase. Bingo!

If you’re not looking for a solution to this problem, you should probably stop reading here. Otherwise, read on—but be warned that I don’t have my configuration files handy, so I may get some of the details wrong. Correct me in the comments, please. You must have mod_rewrite to use these instructions.

So, Apache won’t do it for us. If you want to implement this solution, you have to give up the use of the \<VirtualHost\> directive, and any per-host configuration settings that aren’t allowed in \<Directory\> or \<Location\> sections. Before you do that, note that Apache will allow you to set _one_ virtual host as using SSL, just by adding it to that host’s config and having the host listen on port 443. This is only for two or more hosts; I think in that case Apache will default to the first one it reads.

**Step 0**: disable virtual hosting on port 80. Use `NameVirtualHost *:443` to allow separate settings for SSL connections.

**Step 1**: Add the following sort of code to your main config file. Again, I don’t have mine handy, so I’m giving you the general idea.

```
# This is the site that will be displayed if mod_rewrite isn't enabled
DocumentRoot /var/www/html/main-site

<IfModule rewrite_module>
	RewriteEngine On

	# Change this to the path to your sitemap file (see below)
	RewriteMap sitemap txt:/etc/apache2/sitemap

	# It's this line that may not be correct
	# And getting it wrong can result in infinite loops
	RewriteRule ^ ${sitemap:%{HTTP_HOST}|%{DOCUMENT_ROOT}}%{REQUEST_URI}
</IfModule>

<VirtualHost *:443>
	SSL on
	# fill in the rest of your SSL settings here

	<IfModule rewrite_module>
		RewriteEngine On

		# Change this to the path to your sitemap file (see below)
		RewriteMap sitemap txt:/etc/apache2/sitemap

		# It's this line that may not be correct
		# And getting it wrong can result in infinite loops
		RewriteRule ^ ${sitemap:%{HTTP_HOST}|%{DOCUMENT_ROOT}}%{REQUEST_URI}
	</IfModule>
</VirtualHost>
```

**Step 2**: Create your sitemap file. This is a [rewriting map](http://httpd.apache.org/docs/2.2/mod/mod_rewrite.html#rewritemap) that maps site names to filesystem paths. Mine looks a bit like this, though don’t rely on it for hacking me…

```
# These entries are technically not necessary since it's my DocumentRoot
belkadan.com		/var/www/html/belkadan
www.belkadan.com	/var/www/html/belkadan
# Look! Another "host"!
mail.belkadan.com	/var/www/html/webmail
# etc
```

**Step 3**: Convert your old virtual host specifications over to use \<Directory\>. I think you can handle this on your own, but remember to run a `apache2ctl -t` to see if you’re using any host-specific directives that just don’t apply to \<Directory\> sections. The one that popped up for me was CustomLog; all my logs are back to one monolithic file.

**Step 4**: Reload Apache and hope things don’t break. Test all your sites with both HTTP and HTTPS.

And that’s it! Well…nearly. You can stop here if you want, but if you want special handling of certain locations, you have to implement a namespace system for yourself. I decided that paths starting with `/._` were virtual paths. This actually affects your rewriting rule.

**Step 5**: Change both your rewriting sections to look like this. The `[PT]` parameter means “pass-through” and it sends the rewriting results to other URL-to-filesystem modules like mod_alias.

```
<IfModule rewrite_module>
	RewriteEngine On

	# Change this to the path to your sitemap file (see below)
	RewriteMap sitemap txt:/etc/apache2/sitemap

	# Careful with these lines
	RewriteCond %{REQUEST_URI} !^\/\._	
	RewriteCond ${sitemap:%{HTTP_HOST}|%{DOCUMENT_ROOT}} ^\/\._
	RewriteRule ^ ${sitemap:%{HTTP_HOST}|%{DOCUMENT_ROOT}}%{REQUEST_URI} [PT]

	RewriteCond %{REQUEST_URI} !^\/\._	
	RewriteCond ${sitemap:%{HTTP_HOST}|%{DOCUMENT_ROOT}} !^\/\._
	RewriteRule ^ ${sitemap:%{HTTP_HOST}|%{DOCUMENT_ROOT}}%{REQUEST_URI}
</IfModule>
```

**Step 6**: If you’re using fancy indexing, change all references from `/icons` to `/._icons`. Apache uses the `Alias` directive to resolve the location of the indexing icons, so you need your rewriting system to take that into account.

**Step 7**: Add your special-case sites to the sitemap file. Let’s pretend we’re adding WebDAV capabilities, and for some reason you want it on another host.

```
# all the stuff from before...
webdav.belkadan.com 	/._webdav
```

**Step 8**: Change your special-case virtual hosts to use \<Location\>. This is useful for something like “Dav on” or “Require valid-user”, which you don’t want to do for normal access to your main site! Unfortunately, \<Location\> allows even fewer directives than \<Directory\>, but you can get around this by setting an environment variable and using an \<IfDefine\> later.

**Step 9**: Add an Alias directive for your special-case virtual host.

```
Alias /._webdav /var/www/html/belkadan
```

**Step 10**: Secure your special-case virtual hosts. Right now anyone could access the hypothetical DAV by going to `http://belkadan.com/._webdav`. Block that by adding code like the following:

```
<Location /._webdav>
	# All of your config settings here, then...
	Satisfy all
	SetEnvIf Host ^webdav\.belkadan\.com allow_alias_access
	Allow from env=allow_alias_access
</Location>
```

**Step 11**: `apache2ctl -t`, reload, and test. And at this point you should have a working configuration, with HTTPS available for _all_ of your sites.

I’ll dub this technique “virtual virtual hosting” and leave you with the fallout of the pun. Oh, and I think there’s probably a better way to handle the special cases rather than using a made-up path (a separate host-based SetEnvIf would probably do it), but this is what worked for me.

This entry was posted on [August](https://belkadan.com/blog/2008/08) 28, [2008](https://belkadan.com/blog/2008) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Apache](https://belkadan.com/blog/tags/apache), [Unix](https://belkadan.com/blog/tags/unix)
