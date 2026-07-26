---
title: Updated iTunes Connect Financial Reports to HTML Script
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2009/09/updated-itunes-connect-financial-reports-to-html-script/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:184ecabb36a984ce'
translated: false
---

> 原文：[Updated iTunes Connect Financial Reports to HTML Script](https://oleb.net/blog/2009/09/updated-itunes-connect-financial-reports-to-html-script/)　·　Ole Begemann

# Updated iTunes Connect Financial Reports to HTML Script

A user of my [iTunes Connect Financial Reports to HTML script](https://oleb.net/blog/2009/09/formatting-itunes-connect-financial-reports/) notified me that the script did not work on the file format that Apple used for their Financial Reports before February, 2009. The fix was relatively simple so the new version should support both formats. I used the occasion for a few more changes:

- .
- ERB

  connects the two.
- README.txt

  with some documentation.
- Fixed a bug that caused a crash when calling the script from another folder.
- Moved the whole thing to GitHub.

Please get [the updated code from GitHub](https://github.com/ole/itunesconnect-financialreports). I’d appreciate your feedback and/or bug reports.
