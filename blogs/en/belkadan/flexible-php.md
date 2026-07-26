---
title: Flexible PHP
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2007/03/Flexible-PHP/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:fef3b96399e2ee20'
translated: false
---

> 原文：[Flexible PHP](https://belkadan.com/blog/2007/03/Flexible-PHP/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Inauspicious Beginnings](https://belkadan.com/blog/2007/01/Inauspicious-Beginnings/)

[The Symbolism of Pretty URLS](https://belkadan.com/blog/2007/04/Symbolism-of-Pretty-URLs/) »

## [Flexible PHP](#)

OK, well, if I want to get this off the ground I’ve got to start posting things. Even if I haven’t developed too much lately. So let’s focus on what little I _have_ been doing; that is, working on BlogAgain.

BlogAgain is the name of the software that runs this (blog) site, originally born from a desire for a multi-user blog that actually installed. (At the time, WordPress refused to properly install on the server we were using). Now it just gives me a chance to customize things and offer one more set of PHP-and-MySQL-based blog software to the mix.

Ideally, this would be a very customizable program. But PHP has a lot of quirks that can keep you from being standards-compliant or even flexible…and everything has to be done right in the end. Let’s watch the evolution of a bit of example code that connects to an SQL database, prints the article titles and authors in a given topic, and allows you to choose how to sort them.

```
@mysql_pconnect('localhost', $user, $password, MYSQL_CLIENT_SSL);

$topicID = $_GET['topic'];
$order = $_GET['sort'];
$entries = mysql_query("SELECT title, author FROM entries " .
  "WHERE entries.parent = $topicID ORDER BY $order");

echo '<table>';
    
while ($entry = mysql_fetch_array($entries, MYSQL_ASSOC))
{
  echo '<tr>';
  echo '<td class="postTitle"><a href="blog.php?topic=' . $entry['id'] . '">' .
    $entry['title'] . '</a></td>';
  echo '<td class="postInfo">Started by ' . $entry["author"] . '</td>';
  echo '</tr>';
}

echo '</table>';

echo '<p class="blogNavigation">Sort by: ';
if ($order == 'author')
  echo 'Author / <a href="blog.php?topic=$topicID&sort=title">Title</a>';
else
  echo '<a href="blog.php?topic=$topicID&sort=author">Author</a> / Title';
echo '</p>';
```

Looks OK, right? Unfortunately, just about every other line can get better.

```
@mysql_pconnect('localhost', $user, $password, MYSQL_CLIENT_SSL);
```

I’m not going to fix this one right now, but it would be nice to support at least a few different SQLs, without PHP’s ugly (and not-always-available) PDO interface. A `blogagain_sql_connect($host, $user, $password)` function will do the trick eventually.

```
$topicID = $_GET['topic'];
$order = $_GET['sort'];
```

Do we really care where this came from, or should we be using `$_REQUEST`? I think so, but I may be wrong. Other opinions?

```
$entries = mysql_query("SELECT title, author FROM entries " .
  "WHERE entries.parent = $topicID ORDER BY $order");
```

DANGER DANGER! We just pasted two variables into an SQL query without escaping them! Add `mysql_real_escape_string` to the previous lines, or even better use a `blogagain_sql_escape` function.

```
while ($entry = mysql_fetch_array($entries, MYSQL_ASSOC))
```

This line’s probably OK; the docs say we don’t need to worry about the performance of `mysql_fetch_array`. But we should probably generalize the SQL call again. And yes, we want to loop until all entries are done.

The body of the loop is probably OK. Oh wait! We need to deal with all possibilities of author names, including no name (in which case we want to grab the author’s normal username, rather than the alias saved here) and anonymous users. This code is pretty simple; the real code to print an author is a three-check if statement.

```
echo 'Author / <a href="blog.php?topic=$topicID&sort=title">Title</a>';
```

Uh oh, now we come to the reason I wrote this post! This looks like a perfectly fine link, right? Nope! We’ve got an ampersand (&) in the middle, there. If we want to be XHTML-compliant (and even if we don’t want to confuse a bad HTML parser) we need to change that.

```
echo 'Author / <a href="blog.php?topic=$topicID&amp;sort=title">Title</a>';
```

Better. Oh wait. What if this configuration doesn’t use ampersands to separate query units? That would be…bad…

```
echo 'Author / <a href="blog.php?topic=$topicID' .
  ini_get('arg_separator.output') . 'sort=title">Title</a>';
```

Looking better! But wait, what if, for some strange reason, `arg_separator.output` isn’t set? We need to do a bit better…

```
echo 'Author / <a href="blog.php?topic=$topicID' .
  blogagain_null_check(ini_get('arg_separator.output'), '&') . 'sort=title">Title</a>';

function blogagain_null_check ($data, $alt)
{
    return ($data ? $data : $alt);
}
```

I actually use this function several times, so let’s stick it in an include file. We forgot one thing, though: once again, the & needs to be escaped, or perhaps they decided (for some stupid reason) to use \< as the argument separator. In any case, we need one more addition.

```
echo 'Author / <a href="blog.php?topic=$topicID' .
  htmlspecialchars(blogagain_null_check(ini_get('arg_separator.output'), '&')) .
  'sort=title">Title</a>';
```

There we go. That should provide a bit more flexibility and integrity.

You can see how fast PHP needs to be overhauled, and I didn’t even store any data in the database. Just how far do I have to go to write a whole blog?

This entry was posted on [March](https://belkadan.com/blog/2007/03) 07, [2007](https://belkadan.com/blog/2007) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [PHP](https://belkadan.com/blog/tags/php)
