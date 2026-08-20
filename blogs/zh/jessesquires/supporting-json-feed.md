---
title: 支持 JSON feed
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2017/09/03/supporting-json-feed/'
original_language: en
published: 2017-09-03
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6915a0251de49bf0'
translated: true
---

> 原文：[Supporting JSON feed](https://www.jessesquires.com/blog/2017/09/03/supporting-json-feed/)　·　Jesse Squires

几周前，我终于抽出时间为这个博客增加了对 Brent Simmons 和 Manton Reece 的 [JSON Feed](https://jsonfeed.org/version/1) 的支持。你可以[在此](https://www.jessesquires.com/feed.json)订阅 feed。实现起来既简单又有趣。

> JSON Feed 格式是一种实用的联合格式，类似 [RSS](http://cyber.harvard.edu/rss/rss.html) 和 [Atom](https://tools.ietf.org/html/rfc4287)，但有一个重大区别：它使用 JSON 而非 XML。
> 
> 对于大多数开发者来说，JSON 远比 XML 更容易读写。开发者拿起 XML 解析器可能会抱怨，但解码 JSON 往往只需一行代码。
> 
> 我们希望，由于 JSON 的轻量和 JSON Feed 格式的简洁，开发者会更愿意为开放网络开发。
> 
> — [JSON Feed 版本 1](https://jsonfeed.org/version/1)

采用 JSON Feed 而非 RSS/Atom 等较旧的格式，有着明显的好处。然而，新标准（至少初期）会遭遇[先有鸡还是先有蛋](https://en.wikipedia.org/wiki/Chicken_or_the_egg)的问题：feed 阅读器开发者缺乏支持新版 JSON Feed 格式的动力，因为采用它的发布者很少；而发布者也缺乏采用新格式的动力，因为支持它的 feed 阅读器很少。更何况，发布者已有可用的方案（RSS/Atom）。在这种情况下，我认为发布者需要推动这一改变，最终 feed 阅读器会跟上。好消息是——正如 Brent 和 Manton 明确阐述的那样——处理 [JSON](http://json.org) 既简单又有趣。

### JSON Feed 与 Jekyll

本网站使用 [Jekyll](https://jekyllrb.com) 构建，因此支持 JSON Feed 只需在网站根目录中添加一个新的模板 `feed.json` 文件。这与支持 RSS/Atom 的做法相同，即提供一个 `feed.xml` 模板。你的网站配置可能有所不同，但 `feed.json` 应该与我的类似。[在此查看](https://github.com/jessesquires/jessesquires.com/blob/master/feed.json)。你填入网站元数据，然后遍历每篇文章来构建条目数组。你会发现它与 RSS/Atom 的 [feed.xml](https://github.com/jessesquires/jessesquires.com/blob/master/feed.xml) 相似。

```
---
layout: null
---

{
    "version": "https://jsonfeed.org/version/1",
    "title": "{{ site.title }}",
    "home_page_url": "{{ site.url }}",
    "feed_url": "{{ site.feeds.json | absolute_url }}",
    "description": "{{ site.description }}",
    "icon": "{{ site.logo | absolute_url }}",
    "favicon": "{{ site.favicon | absolute_url }}",
    "expired": false,
    "author": {
        "name": "{{ site.author.name }}",
        "url": "{{ site.url }}",
        "avatar": "{{ site.author.avatar | absolute_url }}"
    },
    "items": [
        {% for post in site.posts %}
        {
            "id": "{{ post.url | absolute_url }}",
            "url": "{{ post.url | absolute_url }}",
            "title": {{ post.title | jsonify }},
            "date_published": "{{ post.date | date_to_xmlschema }}",
            {% if post.date-updated %}
            "date_modified": "{{ post.date-updated | date_to_xmlschema }}",
            {% else %}
            "date_modified": "{{ post.date | date_to_xmlschema }}",
            {% endif %}
            "author": {
                "name": "{{ site.author.name }}",
                "url": "{{ site.url }}",
                "avatar": "{{ site.author.avatar | absolute_url }}"
            },
            "summary": {{ post.excerpt | jsonify }},
            "content_html": {{ post.content | jsonify }}
        }{% if forloop.last == false %},{% endif %}
        {% endfor %}
    ]
}
```

然后，你需要在网站 `<head>` 部分添加一个 `<link />` 标签：

```
<link type="application/json" rel="alternate" href="/feed.json" title="YOUR SITE TITLE" />
```

就这样。当你运行 `jekyll build` 时，就会生成你的[完整 feed](https://www.jessesquires.com/feed.json)。现在，也去为你的博客添加 JSON Feed 支持吧。
