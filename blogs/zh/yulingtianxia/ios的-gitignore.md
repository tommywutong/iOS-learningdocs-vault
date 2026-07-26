---
title: iOS的.gitignore
source: 杨萧玉
source_key: yulingtianxia
source_url: 'http://yulingtianxia.com/blog/2014/04/09/iosde-dot-gitignore/'
original_language: zh
published: 2019-05-26
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:ba1e7eba09122b8b'
translated: n/a
---

> 原文：[iOS的.gitignore](http://yulingtianxia.com/blog/2014/04/09/iosde-dot-gitignore/)　·　杨萧玉

# [iOS的.gitignore](http://yulingtianxia.com/blog/2014/04/09/iosde-dot-gitignore/)

By [杨萧玉](https://plus.google.com/106642427004837273341?rel=author)

发表于 2014-04-09

**文章目录**

在多人一起开发XCode项目的时候，很多中间生成的临时文件并不需要加入到版本控制当中，所以记录下XCode需要用到的`.gitignore`文件

出处：[https://github.com/github/gitignore/blob/master/Objective-C.gitignore](https://github.com/github/gitignore/blob/master/Objective-C.gitignore)

```jboss-cli
# Xcode
#
build/
*.pbxuser
!default.pbxuser
*.mode1v3
!default.mode1v3
*.mode2v3
!default.mode2v3
*.perspectivev3
!default.perspectivev3
xcuserdata
*.xccheckout
*.moved-aside
DerivedData
*.hmap
*.ipa
*.xcuserstate

# CocoaPods
#
# We recommend against adding the Pods directory to your .gitignore. However
# you should judge for yourself, the pros and cons are mentioned at:
# http://guides.cocoapods.org/using/using-cocoapods.html#should-i-ignore-the-pods-directory-in-source-control
#
# Pods/
```

还有需要记住一点的是，使用IB进行界面设计，无论是xib文件还是storyboard，同一时间只能右一个人更改一个Window或VC，虽然XCode5之后xib和storyboard可读性大大增强，但是仍不像Android开发界面的xml格式那么普及，还是小心谨慎为好
