---
title: 快速在多个 Xcode 版本间切换
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2020/07/07/quickly-switching-between-xcodes/'
original_language: en
published: 2020-07-07
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:26f100e334581aa0'
translated: true
---

> 原文：[Quickly switching between Xcodes](https://www.jessesquires.com/blog/2020/07/07/quickly-switching-between-xcodes/)　·　Jesse Squires

为求简洁与整洁，我尽量在同一时间只安装一个 Xcode。但这样的配置很少见，因为我们经常需要同时管理稳定版和 beta 版。

我知道有些人经常会在同一时间安装*多个稳定版*的 Xcode。我可没时间搞这些。我最多只保留两个 Xcode 安装——最新的稳定版和最新的 beta 版（如果有的话）。在 WWDC 期间及之后，当我们有了新的主要（beta）版本 Xcode 时，我发现我需要更频繁地切换，因为 beta 版会以各种方式崩溃，或者我有时需要使用最新的稳定版。

使用普通的 `xcode-select` 很慢，因为你每次都必须提供要选择的 Xcode 的路径。我写了一个自定义的 shell 命令来更快地切换 Xcode。

```
# switch between release and beta xcodes
function xcswitch() {
    RELEASE="Xcode.app"
    BETA="Xcode-beta.app"

    CURRENT=$(xcode-select -p)
    NEXT=""

    if [[ "$CURRENT" =~ "$RELEASE" ]]
    then
        NEXT="$BETA"
    else
        NEXT="$RELEASE"
    fi

    sudo xcode-select -s "/Applications/$NEXT"
    echo "Switched to $NEXT"
}
```

它会检查你当前选中的 Xcode，然后切换到另一个。这有一些假设条件，即你和我一样，只安装了两个 Xcode——`Xcode.app` 和 `Xcode-beta.app`。它还假设它们安装在 `/Applications` 目录下。这个脚本对大多数人应该可以直接使用，但你可以根据自己的需要调整。

如果你觉得有用，可以把它复制到你的 `.bash_profile` 或 `.zprofile` 中，然后通过调用 `xcswitch` 来使用它。

##### [更新](#updated-22-august-2021)  _2021 年 8 月 22 日_

你可以按照 Keith Smiley 的建议，[无需密码即可切换 Xcode 版本](https://www.smileykeith.com/2021/08/12/xcode-select-sudoers/)，让这个方案变得更好。
