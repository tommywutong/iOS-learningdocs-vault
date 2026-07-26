---
title: Swift releases have themes
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2017/03/swift-themed-releases/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:4300e23a156e8910'
translated: false
---

> 原文：[Swift releases have themes](https://oleb.net/blog/2017/03/swift-themed-releases/)　·　Ole Begemann

# Swift releases have themes

About a week ago, [Swift Core Team](https://swift.org/community/#core-team) member Ben Cohen [wrote a thoughtful message](https://forums.swift.org/t/additive-proposals/5312/2) on [swift-evolution](https://swift.org/community/#swift-evolution), answering [a question](https://forums.swift.org/t/additive-proposals/5312) about the chances of purely additive proposals to be accepted for [Swift 4](https://github.com/apple/swift/blob/master/CHANGELOG.md#swift-40).

Ben explains the rationale the Core Team uses to decide which proposals should make it into the next version of the language. The gist of it is that each Swift release should focus on a small number of themes and that proposals contributing to these themes will be given priority.

I think [that post](https://forums.swift.org/t/additive-proposals/5312/2) hasn’t received the attention it deserves, which is why I’m quoting it here in its entirety (links and emphasis added by me):

> It’s worth noting that some additive proposals are currently in scope, where they are aligned with [the themes set out for Swift 4](https://forums.swift.org/t/looking-back-on-swift-3-and-ahead-to-swift-4/3610). For example, additive proposals for [`String`](https://developer.apple.com/reference/swift/string), [`Dictionary`](https://developer.apple.com/reference/swift/dictionary) and [`Sequence`](https://developer.apple.com/reference/swift/sequence)/[`Collection`](https://developer.apple.com/reference/swift/collection) are being accepted for the standard library. In upcoming releases of Swift, it is likely that additive proposals aligned with other themes, such as further string work (like native regexes), move-only types, concurrency, reflection, or further generics enhancements, will be in scope. _We feel that keeping the focus on specific themes is really important for the evolution of the language, and that unconstrained additive proposals not associated with any current theme are always going to have a very high bar for acceptance._
> 
> One reason is bandwidth, both of the core team and of the community. Keeping the discussion focused on themes helps other community participants follow the mailing list (though hopefully a [move to a message board format](https://forums.swift.org/t/plan-to-move-swift-evolution-and-swift-users-mailing-lists-to-discourse/5128) will help with this some). And by ensuring proposals are themed with the overall goals of each release, we stand a higher chance of avoiding a build-up of proposals that are accepted, but then not actually implemented.
> 
> Moreover, when discussions are focused on specific themes, _we can provide a more complete, coherent design for the features within that theme_. We can explore how (say) all of the [new generics features of Swift 4](https://github.com/apple/swift/blob/master/CHANGELOG.md#swift-40) fit together to provide a complete, coherent system that is easier to use and explain, or how all of the new string features fit together to make [Awesome Strings](https://github.com/apple/swift/blob/master/docs/StringManifesto.md). _It’s partly about messaging—what does Swift 4 bring to the table?—and partly about giving us a better chance at building a coherent design._
> 
> The coherent design is important both within the release—because it makes it easier for developers to learn to use the new features together—_but also for the long-term health of the language_. Without theming proposals, it is very difficult to see how an individual proposal fits into the overall direction of Swift. We would run the risk of making small local changes that we later regret when considering wider-reaching changes to which they are related. There is also a risk of not noticing the accretion of too many keywords or concepts in the language that individually make sense but overall don’t fit well together.
> 
> For example, recent proposals around [refactoring of meta types](https://github.com/DevAndArtist/swift-evolution/blob/refactor_existential_metatypes/proposals/0126-refactor-metatypes.md) really need to be considered in the wider context of reflection as a whole so should probably wait until that theme is in scope. Another example: the recent proposal [SE-154](https://github.com/apple/swift-evolution/blob/master/proposals/0154-dictionary-key-and-value-collections.md) to change the types for the keys and values collections on `Dictionary` did not really make sense in isolation—it still only provided a slightly clunky way to solve the problem where dictionaries need an “initial” value, and then update that value in-place. But it needed to be considered as part of the [ABI stability](https://github.com/apple/swift/blob/master/docs/ABIStabilityManifesto.md) theme. It was partly for this reason we decided to [open up a wider discussion](https://forums.swift.org/t/dictionary-enhancements/5204) of `Dictionary` for [stage 2](https://forums.swift.org/t/swift-4-stage-2-starts-now/5203).
> 
> For [Swift 3](https://github.com/apple/swift-evolution/blob/master/releases/swift-3_0.md) and [Swift 4](https://forums.swift.org/t/looking-back-on-swift-3-and-ahead-to-swift-4/3610), the core team set out the themes for each release. _The core team would like to involve the community earlier in the process to help define the themes for future releases, but are still thinking about the best way to do so._

Swift 4.0 is still half a year away, but it’s never too soon to start speculating what the themes of Swift 5 will be. Surely [ABI stability](https://github.com/apple/swift/blob/master/docs/ABIStabilityManifesto.md), but what else? More string refinements? Concurrency? Reflection?
