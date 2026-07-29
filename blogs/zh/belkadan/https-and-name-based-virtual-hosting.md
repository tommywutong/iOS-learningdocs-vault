---
title: HTTPS 与基于名称的虚拟主机
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2008/08/HTTPS-and-Name-based-Virtual-Hosting/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:948f171e58614f3d'
translated: true
---

> 原文：[HTTPS and Name-based Virtual Hosting](https://belkadan.com/blog/2008/08/HTTPS-and-Name-based-Virtual-Hosting/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [无 App 的提醒（或 nib）](https://belkadan.com/blog/2008/03/Alerts-Without-Apps/)

[Objective-J and Objective-C](https://belkadan.com/blog/2008/09/Objective-J-and-Objective-C/) »

[在共享主机上设置 gitweb](https://belkadan.com/blog/2020/01/Gitweb-on-Shared-Hosting/?tag=apache) »

« [端口 25 被阻止？](https://belkadan.com/blog/2007/07/Port-25-Blocked/?tag=unix)

[Z shell](https://belkadan.com/blog/2009/06/Z-shell/?tag=unix) »

## [HTTPS 与基于名称的虚拟主机](#)

如果你自己运行服务器已经有一段时间，最终你会开始产生隐私（privacy）方面的顾虑，想要使用 HTTPS。届时，如果你只运行单个站点，你可以轻松愉快地设置好；否则你就会沮丧地发现，无法在基于名称的虚拟主机（name-based virtual host）上使用 HTTPS。引用 Apache 站点上的说法：

> 原因非常技术性，有点类似“先有鸡还是先有蛋”的问题。SSL 协议层位于 HTTP 协议层之下，并封装了 HTTP。当建立 SSL 连接（HTTPS）时，Apache/mod_ssl 必须与客户端协商 SSL 协议参数。为此，mod_ssl 需要查询虚拟服务器的配置（例如，它需要查找加密套件、服务器证书等）。但为了到达正确的虚拟服务器，Apache 又必须先知道 Host HTTP 头部字段。要做到这一点，就需要读取 HTTP 请求头部。这在 SSL 握手完成之前是无法做到的，但完成 SSL 握手阶段又需要这些信息。明白了吧！

如果你不是在寻找这个问题的解决方案，也许应该就此打住。否则，请继续读下去——但请注意，我手边没有现成的配置文件，所以可能会遗漏一些细节。欢迎在评论中纠正我。要使用这些说明，你必须有 `mod_rewrite`。

所以，Apache 是不会帮我们做这件事的。如果你想要实现这个解决方案，就必须放弃使用 \<VirtualHost\> 指令，以及任何不允许在 \<Directory\> 或 \<Location\> 区段中使用的按主机配置的设置。在这样做之前，请注意 Apache 允许你为 _一个_ 虚拟主机设置 SSL——只需将该主机的配置添加进去，并让该主机监听 443 端口即可。这只适用于两个或更多主机的情况；我相信在这种情况下，Apache 会默认使用它读取到的第一个主机。

**第 0 步**：禁用端口 80 上的虚拟主机。使用 `NameVirtualHost *:443` 来允许为 SSL 连接设置独立的配置。

**第 1 步**：在你的主配置文件中添加类似下面的代码。再说一次，我手边没有现成的配置，所以只给出大致思路。

```
# 如果未启用 mod_rewrite，将显示此站点
DocumentRoot /var/www/html/main-site

<IfModule rewrite_module>
	RewriteEngine On

	# 将此路径改为你的 sitemap 文件的路径（见下文）
	RewriteMap sitemap txt:/etc/apache2/sitemap

	# 这一行可能不正确
	# 弄错可能导致无限循环
	RewriteRule ^ ${sitemap:%{HTTP_HOST}|%{DOCUMENT_ROOT}}%{REQUEST_URI}
</IfModule>

<VirtualHost *:443>
	SSL on
	# 在此填写其余的 SSL 设置

	<IfModule rewrite_module>
		RewriteEngine On

		# 将此路径改为你的 sitemap 文件的路径（见下文）
		RewriteMap sitemap txt:/etc/apache2/sitemap

		# 这一行可能不正确
		# 弄错可能导致无限循环
		RewriteRule ^ ${sitemap:%{HTTP_HOST}|%{DOCUMENT_ROOT}}%{REQUEST_URI}
	</IfModule>
</VirtualHost>
```

**第 2 步**：创建你的 sitemap 文件。这是一个[重写映射（rewriting map）](http://httpd.apache.org/docs/2.2/mod/mod_rewrite.html#rewritemap)，将站点名称映射到文件系统路径。我的文件看起来有点像这样，不过不要指望靠它黑我……

```
# 这些条目技术上并非必需，因为这是我的 DocumentRoot
belkadan.com		/var/www/html/belkadan
www.belkadan.com	/var/www/html/belkadan
# 看！另一个“主机”！
mail.belkadan.com	/var/www/html/webmail
# 等等
```

**第 3 步**：将你旧的虚拟主机规范转换为使用 \<Directory\>。我相信你可以自己处理，但记得运行 `apache2ctl -t` 来检查你是否使用了某些特定于主机而不适用于 \<Directory\> 区段的指令。我遇到的这种指令是 `CustomLog`；我的所有日志都恢复到了单一的汇总文件。

**第 4 步**：重新加载 Apache，希望一切正常。使用 HTTP 和 HTTPS 测试你的所有站点。

就是这样！嗯……差不多。如果你愿意，可以在此停步。但如果你需要对某些特定路径做特殊处理，就必须为自己实现一个命名空间（namespace）系统。我决定以 `/._` 开头的路径作为虚拟路径。这实际上会影响你的重写规则。

**第 5 步**：将你的两个重写区段都改成这样。`[PT]` 参数表示“直通”，它会将重写结果传递给其他 URL 到文件系统的模块，比如 `mod_alias`。

```
<IfModule rewrite_module>
	RewriteEngine On

	# 将此路径改为你的 sitemap 文件的路径（见下文）
	RewriteMap sitemap txt:/etc/apache2/sitemap

	# 注意这几行
	RewriteCond %{REQUEST_URI} !^\/\._	
	RewriteCond ${sitemap:%{HTTP_HOST}|%{DOCUMENT_ROOT}} ^\/\._
	RewriteRule ^ ${sitemap:%{HTTP_HOST}|%{DOCUMENT_ROOT}}%{REQUEST_URI} [PT]

	RewriteCond %{REQUEST_URI} !^\/\._	
	RewriteCond ${sitemap:%{HTTP_HOST}|%{DOCUMENT_ROOT}} !^\/\._
	RewriteRule ^ ${sitemap:%{HTTP_HOST}|%{DOCUMENT_ROOT}}%{REQUEST_URI}
</IfModule>
```

**第 6 步**：如果你使用了 fancy 索引（fancy indexing），将所有对 `/icons` 的引用改为 `/._icons`。Apache 使用 `Alias` 指令解析索引图标的位置，因此你需要重写系统来处理这一点。

**第 7 步**：将你的特殊用例站点添加到 sitemap 文件中。假设我们要添加 WebDAV 功能，并且出于某种原因希望它在另一个主机上。

```
# 之前的所有内容...
webdav.belkadan.com 	/._webdav
```

**第 8 步**：将你的特殊用例虚拟主机改为使用 \<Location\>。这对于像“Dav on”或“Require valid-user”这样的设置很有用——你肯定不希望普通访问你的主站点时也要求这些配置！不幸的是，\<Location\> 允许的指令甚至比 \<Directory\> 更少，但你可以通过设置一个环境变量（environment variable）并在之后使用 \<IfDefine\> 来绕过这个限制。

**第 9 步**：为你的特殊用例虚拟主机添加一个 `Alias` 指令。

```
Alias /._webdav /var/www/html/belkadan
```

**第 10 步**：保护你的特殊用例虚拟主机。目前任何人都可以通过访问 `http://belkadan.com/._webdav` 来访问假设的 DAV。通过添加如下代码来阻止这种情况：

```
<Location /._webdav>
	# 在此填写所有配置设置，然后...
	Satisfy all
	SetEnvIf Host ^webdav\.belkadan\.com allow_alias_access
	Allow from env=allow_alias_access
</Location>
```

**第 11 步**：运行 `apache2ctl -t`，重载并测试。至此，你应该拥有一个可正常运行的配置，并可以为 _所有_ 站点提供 HTTPS 支持。

我将这种技术称为“虚拟虚拟主机”（virtual virtual hosting），并把这个双关语的后果留给你。哦，还有，我觉得可能有一种更好的方法来处理特殊情况，而不必使用虚构的路径（单独的基于主机的 `SetEnvIf` 可能就能做到），但这是对我有效的方法。

本文发表于 [2008 年](https://belkadan.com/blog/2008) [8 月](https://belkadan.com/blog/2008/08) 28 日，归类于 [技术](https://belkadan.com/blog/technical)。标签：[Apache](https://belkadan.com/blog/tags/apache)、[Unix](https://belkadan.com/blog/tags/unix)
