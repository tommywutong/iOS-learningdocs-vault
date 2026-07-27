---
title: 用rss2email閱讀feeds
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2011-07-20-read-feeds-with-rss2email'
original_language: en
published: 2011-07-20
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6e8d566ff7a43502'
translated: false
---

> 原文：[用rss2email閱讀feeds](https://maskray.me/blog/2011-07-20-read-feeds-with-rss2email)　·　MaskRay (宋方睿)

[2011-07-20](https://maskray.me/blog/2011-07-20-read-feeds-with-rss2email)

# 用rss2email閱讀feeds

很久沒用rss的閱讀器了，以前曾用過 emacs 的 newsticker ，不支持HTML。也用過Google Reader，打開速度太慢，而且對Pentadactyl不友好。

## 把feeds轉成郵件來閱讀

我的想法是找一款工具，把feeds轉換成郵件，由本地的_procmail_處理（歸類），然後再用_mutt_閱讀。

### rss2email

rss2email就是這樣一個能把feeds轉成郵件的工具，Python寫的，可以通過SMTP把郵件投遞給服務器或者把郵件轉交給MTA。可惜的是它沒法像getmail或是fetchmail那樣，指定用於處理郵件的程序。

它的使用還是比較簡單的，配置只有兩歩：

- _r2e new user@example.org_ ，轉換得到的 feeds 默認投遞到`user@example.org`
- _r2e add http://feed.url/somewhere.rss_ ，訂閱一個源

以後只要運行_r2e run_就能把新的feeds轉成郵件發送給你配置時設置的郵箱。我把這條命令寫到了=crontab=裏。

### 原來的設想

我最初設想是安裝個MTA，比如postfix，_r2e_把郵件交給MTA，MTA把收到的郵件交給procmail。但這樣略顯麻煩，MTA的配置挺麻煩的，還得讓它開機自動啓動。

### 能否繞過 MTA 呢

我決定修改rss2email的源碼來避免 MTA 。rss2email的源碼是比較簡單的，在`/usr/lib/python2.7/site-packages/rss2email/main.py`中搜索`sendmail`就找到了這樣一行：

```python
p = subprocess.Popen(["/usr/sbin/sendmail", recipient], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
```

不難看出 recipient 就是指定的郵箱。比如 recipient 是 ray@localhost ，它會調用 _/usr/sbin/sendmail ray@localhost_ 來把郵件轉交給 _sendmail_ (/MTA/)。

只要把這行改成：

```python
p = subprocess.Popen(["/usr/bin/procmail", "-d", recipient], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
```

r2e就會直接把郵件交給_procmail_了。

### 具體配置

- 修改`/usr/lib/python2.7/site-packages/rss2email/main.py`
- _r2e new ray_ ， ray 是我的用戶名
- _r2e add_ http://feed.url1/somewhere.rss
- _r2e add_ http://feed.url2/somewhere.rss
- _r2e add_ http://feed.url3/somewhere.rss
- 配置 _procmail_ ，根據郵件頭的 User-Agent 和 X-RSS-Feed 信息來決定投遞到哪個 maildir/mbox 。
- 把 _r2e run_ 加入 crontab

下面是我添加到 ~/.procmailrc 中的內容：

```
:0
* ^User-Agent: rss2email
{
  :0
  * ^X-RSS-Feed: http://news.ycombinator.com/rss
  rss/hacker-news/

  :0
  * ^X-RSS-Feed: http://solidot.org.feedsportal.com/c/33236/f/556826/index.rss
  rss/solidot/

  :0
  * ^X-RSS-Feed: http://feeds.feedburner.com/linuxtoy
  rss/linuxtoy/

  :0
  * ^X-RSS-Feed: http://jandan.net/feed
  rss/jandan/
}
```

## 2014年11月26日更新

這個方案已廢棄，改用newsbeuter閱讀rss了。
