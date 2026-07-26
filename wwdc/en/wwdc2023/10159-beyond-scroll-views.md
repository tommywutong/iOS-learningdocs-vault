---
title: Beyond scroll views
session_id: 10159
collection: wwdc2023
year: 2023
duration: '14:46'
topics: ['SwiftUI & UI Frameworks']
group: E · UIKit/SwiftUI 渲染与 UI 性能
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2023/10159/'
content_hash: 'sha256:a1493db1358d1fb2'
translated: false
---

# Beyond scroll views

<sub>WWDC2023 · 14:46 · SwiftUI & UI Frameworks</sub>

Find out how you can take your scroll views to the next level with the latest APIs in SwiftUI. We'll show you how to customize scroll...

> [!note] 归档理由
> 滚动视图的底层行为与几何

## Chapters

- [Introduction to scroll views](/videos/play/wwdc2023/10159/?time=0)
- [Margins and safe area](/videos/play/wwdc2023/10159/?time=121)
- [Targets and positions](/videos/play/wwdc2023/10159/?time=254)
- [Scroll transitions](/videos/play/wwdc2023/10159/?time=693)

## Resources

- [Introduction to scroll views](https://developer.apple.com/videos/play/wwdc2023/10159/?time=0)
- [Margins and safe area](https://developer.apple.com/videos/play/wwdc2023/10159/?time=121)
- [Targets and positions](https://developer.apple.com/videos/play/wwdc2023/10159/?time=254)
- [Scroll transitions](https://developer.apple.com/videos/play/wwdc2023/10159/?time=693)
- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10159/4/DCE1F4A7-9E0E-4F48-B70A-6C44D758769E/downloads/wwdc2023-10159_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10159/4/DCE1F4A7-9E0E-4F48-B70A-6C44D758769E/downloads/wwdc2023-10159_sd.mp4?dl=1)
- [Explore pie charts and interactivity in Swift Charts](https://developer.apple.com/videos/play/wwdc2023/10037)
- [What’s new in SwiftUI](https://developer.apple.com/videos/play/wwdc2023/10148)
- [ScrollView](https://developer.apple.com/videos/play/wwdc2023/10159/?time=46)
- [Basic Featured Section](https://developer.apple.com/videos/play/wwdc2023/10159/?time=149)
- [Featured Section with Margins](https://developer.apple.com/videos/play/wwdc2023/10159/?time=240)
- [Featured Section + Container Relative Frame](https://developer.apple.com/videos/play/wwdc2023/10159/?time=462)
- [Featured Section + Scroll Position](https://developer.apple.com/videos/play/wwdc2023/10159/?time=586)
- [Featured Section + Scroll Transition](https://developer.apple.com/videos/play/wwdc2023/10159/?time=754)

## Transcript

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ ♪ Harry: Hi, I'm Harry, an engineer on the SwiftUI team. Welcome to Beyond Scroll Views where I'll talk about some new improvements to scroll views in SwiftUI. The things our devices want to do can rarely be contained within their fixed screen sizes. One way they handle this complexity is by introducing scrolling. This allows them to show us everything that won't fit on screen. SwiftUI offers a few different components that let you integrate scrolling into your own apps. Today, I'll be talking about one of those components. ScrollView. A ScrollView is a building block that lets your content scroll. Scroll views have axes that defines the directions in which they're scrollable. Scroll views have content. When that content exceeds the size of the ScrollView, some of that content will be clipped, and people will need to scroll to reveal it. Scroll views ensure that the content is placed within the safe area by resolving the safe area into margins outsetting its content. A ScrollView evaluates its content eagerly by default. You can change this behavior by using a lazy stack.

The exact position of where the ScrollView is scrolled within the content is called the content offset. SwiftUI has offered the ScrollViewReader API as a way to control the content offset. This year, SwiftUI is introducing more ways to both influence and react to the content offset managed by a ScrollView. In this talk, I'll start by discussing ways to influence a ScrollView's margins and how they relate to safe areas. I'll then talk about managing a ScrollView's content offset through scroll targets and scroll positions. Finally, I'll show off how you can add some real flair to your apps with scroll transitions. Ever since I started making my Colors app, my users have really liked showing me some of their favorite color combinations. I'd like to feature some of these combinations so that other people can enjoy them. To do this, I've been working on adding a gallery feature to my Colors app. I've already made some progress implementing my gallery. Throughout this talk I'll be polishing both the header and content of the featured section of my gallery.

In my gallery, I have a horizontal ScrollView wrapping a lazy stack. I'll first make this view look a bit nicer with some margins. Your first instinct might be to add some padding to a ScrollView, and this will inset a ScrollView, but notice that now its content is clipped when scrolling. Instead of insetting the ScrollView itself, I'd like to extend the content margins of the ScrollView. I can do that with the new safe area padding modifier. This behaves like the normal padding modifier, but instead of padding the content, it adds the padding to the safe area. Now my ScrollView expands the whole width, which lets the next item peek out. Before I go further, I'd talk a little about safe areas in relation to ScrollView’s. Safe areas most commonly come from the device your app is running on. The can also come from APIs like the safe area padding or safe area inset modifier. A ScrollView resolves the safe area into the margins it applies to its content. This includes content you are responsible for, but also additional content that the ScrollView is responsible for like scroll indicators. This means it's not possible to configure different insets for different kinds of content by modifying the safe area.

If you want to apply different insets, you can use the new contentMargins API. This API allows you to inset the content of the ScrollView separately from the scroll indicators. Or inset the indicators separately from the content. Going back to my gallery, I'll update my safe area padding modifier to use the content margin API. Now that my views have a bit of margins applied, one of the things I'd like to do is control what content offset the ScrollView will scroll to once someone lifts their finger.

By default, a ScrollView uses a standard deceleration rate along with the velocity of the scroll to calculate the target content offset the scroll should end at. It does not take into account things like the size of the ScrollView or its content. But sometimes those things matter. New in SwiftUI, you can change how a ScrollView calculates this target content offset with the scrollTargetBehavior modifier. This modifier takes a type conforming to the scrollTargetBehavior protocol. Here I've specified the paging behavior. Now my ScrollView swipes one page at a time. The paging behavior is special. It has a custom deceleration rate and chooses where to scroll based on the containing size of the ScrollView itself. This works well for iOS, but becomes a little bit much on the larger screens of iPadOS. Instead of aligning to the containing size of the ScrollView, I'd like to align to individual views.

The view aligned behavior aligns the ScrollView to views, so the ScrollView needs to know which views it should consider for alignment. These views are called scroll targets, and there's a new family of modifiers that let me specify which views are scroll targets. Here I'll use the scroll target layout modifier to have each hero view in the lazy stack be considered a scroll target. You can also mark individual views as targets using the scroll target modifier. But when using lazy stacks, it's important to use the scroll target layout modifier. Views outside the visible region have not yet been created. The layout knows about which views it will create, though, so it can make sure the ScrollView scrolls to the right place.

Now my ScrollView is looking a lot better on iPad. The paging and view aligned behaviors are built off of the new ScrollTargetBehavior protocol. While SwiftUI provides these common behaviors for you, it also allows you to conform your own types to this protocol and implement your own custom behavior, much like you would adopt the previously introduced layout protocol.

Conform your own types to the ScrollTargetBehavior by implementing the one required method: updateTarget. SwiftUI calls this method when calculating where a scroll should end, but also in other contexts like when the ScrollView changes size. Customizing the behavior is easy. Here if the target is close to the top of the ScrollView, and the scroll was flicked up, I'll prefer to scroll to the exact top of the ScrollView by modifying the provided target. This will result in the ScrollView choosing a different content offset to be the end point of the scroll. And that's all it takes to insert my own custom code for influencing where a ScrollView chooses to scroll.

Let's go back to my gallery view. I'd like to talk about layout. Notice that my hero view is sized in relation to the overall width of the device. And if we look at iPad, two views fit evenly within the device's width. Previously you would've had to use a GeometryReader to accomplish this, but this year SwiftUI makes this much easier with a new API called the containerRelativeFrame modifier.

I'll show you how my hero view uses this API. I'll start with a stack of color views, along with a frame modifier specifying a fixed height. I'll add the containerRelativeFrame modifier to my view. Here I specify the horizontal axis, which lets the view just take on the width of its container. In my case the container will be the surrounding ScrollView, but it might also be the nearest column of a navigation split view, or the window of your app.

When the width of my container changes, the size of my views automatically update. I can create a grid-like layout of these views by providing a count and spacing. I can conditionalize the count based on the horizontal sizeClass to have two columns on iPad and one column on phone. What's even better is that I can remove the OS conditionals as the horizontal sizeClass environment property is now available on all platforms. Finally, I'll use the aspectRatio modifier to have a height relative to the width, instead of hardcoding a fixed height. So I've gotten the layout and scroll behavior of my gallery done. There's some more changes I'd like to make. One thing you'll notice are the scroll indicators. I'd like to remove those.

I can use the existing scrollIndicators API to accomplish this. This looks great when swiping my finger on an iPad, but I often use my gallery on a Mac. And on a Mac, I might not be able to easily perform a horizontal swipe gesture like when using a mouse or other input devices. And when I connect a mouse, the indicators are visible, even though I've requested they be hidden. Using a mouse can make scrolling difficult or impossible without scroll indicators. For this reason, the default behavior of the scrollIndicators modifier is to hide the indicators when using more flexible input devices, like trackpads, but to allow the indicators to show when a mouse is connected. You can provide a value of never to the scrollIndicators modifier to always hide the indicators regardless of input device. But my app still needs to support people who use a mouse. So I'll need to provide an alternative means to scroll my gallery for them. Instead of scroll indicators, I'll render some views that allow users to scroll to the previous or next views with a click. To start building that, let's clean my ScrollView up a bit. I'll move my ScrollView into a VStack with my header view.

Now I'll focus on the header view.

I'll add some custom paddle views into the header view. In past versions of SwiftUI, I would have reached for a ScrollViewReader to pass to my paddles and scroll to the appropriate view. New in SwiftUI, though, is the scrollPosition modifier. This modifier associates a binding to a state wrapping an identifier. I'll pass that to my scrollPosition modifier which the ScrollView will read from and to my header view. In the paddles of my header view, I can write to the binding like any other piece of state. When the binding is written to, the ScrollView will scroll to the view with that ID. Just like the view aligned ScrollTargetBehavior, the scroll position modifier uses the scroll target layout modifier to know which views to consider for querying their identity values.

The scroll position modifier also allows me to know the identity of the view currently scrolled. So I can add to my header view some text that shows the value of the hero image currently scrolled. When the most leading view in my ScrollView changes, the binding automatically updates. Now my mouse users can scroll through my gallery. There's one last bit of polish I'd like to add to this view. Just like its useful to know which view is currently scrolled, sometimes I want to visually alter a view based on where it is within the ScrollView. There's new API called ScrollTransitions in SwiftUI that make this really easy. A ScrollTransition is a lot like a normal transition. A transition describes the changes a view should undergo when its appearing or disappearing. When a view has appeared, it's in its identity phase where no customizations should be applied. A ScrollTransition describes a similar set of changes as a transition but instead applies those as a view enters the visible region of a ScrollView and then leaves the visible region.

By default, when the view is in the center of the visible region, it's in the identity phase of the ScrollTransition. Let's look at this in the context of my hero view. I'll clean this up a bit to focus on ScrollTransitions.

As a view gets near the edges of the ScrollView, I'd like it to scale down a bit in size. I'll start by adding the scrollTransition modifier. This API takes content and a phase and allows you to specify visual changes to the content based on the phase. Here I'll specify a decrease in scale when the view is not in its identity phase.

That looks great! ScrollTransitions work with a new protocol called VisualEffect. This protocol provides a set of customizations for view content that are safe to use as functions of layout like the content offset of a ScrollView. Many of them might look familiar to you. You already know about the scaleEffect. You can also customize the rotation, or the offset much like you would with view modifiers. However, not all view modifiers can be safely used inside of a scrollTransition. For example, customizing the font is not supported and will not build. Anything that will change the overall content size of the ScrollView cannot be used within a scrollTransition modifier. Wow, we've covered a lot so let's do a quick review.

We talked about the differences between safe areas and contentMargins and their relationship to ScrollViews. I showed you how you can use the paging and view aligned scrollTargetBehaviors to influence how a ScrollView behaves and how you can write your own conformances to the scrollTargetBehavior protocol. You learned about how much easier it is to create layouts relative to their container using the containerRelativeFrame modifier. I hooked into the state of a ScrollView using the scrollPosition modifier, allowing me to both programmatically scroll and be informed of which view is currently scrolled. And finally, I created visual effects based on the content offset of my ScrollView with the scrollTransition API. I hope you've enjoyed learning about these improvements to ScrollViews. Thanks, and have a great WWDC. ♪ ♪
