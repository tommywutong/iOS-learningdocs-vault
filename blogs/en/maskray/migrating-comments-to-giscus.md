---
title: Migrating comments to giscus
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2025-02-17-migrating-comments-to-giscus'
original_language: en
published: 2025-02-17
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6fd90e2696ce9c5f'
translated: false
---

> 原文：[Migrating comments to giscus](https://maskray.me/blog/2025-02-17-migrating-comments-to-giscus)　·　MaskRay (宋方睿)

[2025-02-17](https://maskray.me/blog/2025-02-17-migrating-comments-to-giscus)

# Migrating comments to giscus

Followed this guide: [https://www.patrickthurmond.com/blog/2023/12/11/commenting-is-available-now-thanks-to-giscus](https://www.patrickthurmond.com/blog/2023/12/11/commenting-is-available-now-thanks-to-giscus)

Add the following to `layout/_partial/article.ejs`

```plaintext
<% if (!index && post.comments) { %>
<section class="giscus"></section>
<script src="https://giscus.app/client.js"
 data-repo="MaskRay/maskray.me"
 data-repo-id="FILL IT UP"
 data-category="Blog Post Comments"
 data-category-id="FILL IT UP"
 data-mapping="pathname"
 data-strict="0"
 data-reactions-enabled="1"
 data-emit-metadata="0"
 data-input-position="bottom"
 data-theme="preferred_color_scheme"
 data-lang="en"
 data-loading="lazy"
 crossorigin="anonymous"
 async>
</script>
<% } %>
```

Unfortunately comments from Disqus have not been migrated yet. If you've left comments in the past, thank you. Apologies they are now gone.

While you can create Github Discussions via GraphQL API, I haven't found a solution that works out of the box. [https://www.davidangulo.xyz/posts/dirty-ruby-script-to-migrate-comments-from-disqus-to-giscus/](https://www.davidangulo.xyz/posts/dirty-ruby-script-to-migrate-comments-from-disqus-to-giscus/) provides a Ruby solution, which is promising but no longer works.

```plaintext
Failed to define value method for :name, because EnterpriseOrderField already responds to that method. Use `value_method:` to override the method name or `value_method: false` to disable Enum value me
thod generation.
Failed to define value method for :name, because EnvironmentOrderField already responds to that method. Use `value_method:` to override the method name or `value_method: false` to disable Enum value m
ethod generation.
Failed to define value method for :name, because LabelOrderField already responds to that method. Use `value_method:` to override the method name or `value_method: false` to disable Enum value method
generation.
...
.local/share/gem/ruby/3.3.0/gems/graphql-client-0.25.0/lib/graphql/client.rb:338:in `query': wrong number of arguments (given 2, expected 1) (ArgumentError)
        from g.rb:42:in `create_discussion'
```
