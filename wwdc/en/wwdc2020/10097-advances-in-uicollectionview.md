---
title: Advances in UICollectionView
session_id: 10097
collection: wwdc2020
year: 2020
duration: '9:55'
topics: ['SwiftUI & UI Frameworks']
group: E · UIKit/SwiftUI 渲染与 UI 性能
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2020/10097/'
content_hash: 'sha256:cb83f936c7006b6d'
translated: false
---

# Advances in UICollectionView

<sub>WWDC2020 · 9:55 · SwiftUI & UI Frameworks</sub>

Learn about new features of UICollectionView that make it easier to use and unlock powerful new functionality. We'll show you how to use...

> [!note] 归档理由
> UICollectionView 增强

## Resources

- [Implementing modern collection views](https://developer.apple.com/documentation/UIKit/implementing-modern-collection-views)
- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10097/3/CE693EFF-2BF8-4B42-B483-04F69015A601/wwdc2020_10097_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10097/3/CE693EFF-2BF8-4B42-B483-04F69015A601/wwdc2020_10097_sd.mp4?dl=1)
- [Make blazing fast lists and collection views](https://developer.apple.com/videos/play/wwdc2021/10252)
- [Build for iPad](https://developer.apple.com/videos/play/wwdc2020/10105)
- [Lists in UICollectionView](https://developer.apple.com/videos/play/wwdc2020/10026)
- [Modern cell configuration](https://developer.apple.com/videos/play/wwdc2020/10027)
- [Advances in Collection View Layout](https://developer.apple.com/videos/play/wwdc2019/215)
- [Advances in UI Data Sources](https://developer.apple.com/videos/play/wwdc2019/220)
- [UICollectionViewCompositionalLayout Lists](https://developer.apple.com/videos/play/wwdc2020/10097/?time=375)
- [Cell Registration](https://developer.apple.com/videos/play/wwdc2020/10097/?time=453)
- [.cell Content Configuration](https://developer.apple.com/videos/play/wwdc2020/10097/?time=512)
- [.valueCell Content Configuration](https://developer.apple.com/videos/play/wwdc2020/10097/?time=518)
- [.subtitleCell Content Configuration](https://developer.apple.com/videos/play/wwdc2020/10097/?time=524)

## Transcript

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

Hello and welcome to WWDC.

Welcome. My name is Steve Breen, and I'm an engineer on the UIKit team. In this video, we're going to chat a bit about advances in UICollectionView for iOS 14.

Before we dive into our content, I'm gonna highlight a portion of the companion sample project for this video, entitled Emoji Explorer.

This sample has a lot of interesting components baked in to its design. In this first section, there's a horizontally scrolling grid of emoji. This is a pretty common design element in today's applications. Now, this middle section of Emoji Explorer is especially novel. It's an expandable-collapsible outline, which is new in iOS 14.

And finally, in this last section, there's a design that looks suspiciously like a UITableView right here, camped out in the middle of our UICollectionView.

Okay, so that's Emoji Explorer. And we'll be referring back to this throughout the video.

The APIs that comprise UICollectionView can be slotted into three distinct categories-- Data, Layout and Presentation. One of the novel concepts UICollectionView was built on was the separation of concerns between the data, or the "what," from the layout, the "where" content is being rendered. This distinction is at the core of what makes UICollectionView so flexible.

When UICollectionView was first released back in iOS 6, data was managed via an indexPath-based protocol, UICollectionViewDataSource.

For layout we had an abstract class, UICollectionViewLayout, and we shipped a concrete subclass, UICollectionViewFlowLayout.

And on the presentation side, we published two view types-- UICollectionViewCell and UICollectionReusableView.

Back in iOS 13, we introduced two new components for Data and Layout respectively with Diffable Data Source and Compositional Layout. These are APIs to use for building apps with UICollectionViews today.

For iOS 14, we built on these modern APIs and introduced new features across all three of these API categories with enhancements to Diffable Data Sources, Compositional Layout and cells.

First up, let's chat about enhancements to Diffable Data Source.

Diffable Data Source, introduced in iOS 13, greatly simplifies the management of UI State through the addition of the new snapshot data type.

Snapshots encapsulate the entire UI State via the use of unique section and item identifiers.

When updating a UICollectionView, we first create a new snapshot, populate it with the current UI State and then apply it to the data source.

Diffable Data Source computes the differences and generates animations automatically without requiring any additional work from you.

So we covered this API in detail in the WWDC 2019 video "Advances in UI Data Sources." And I encourage you to check out that video to learn more.

For iOS 14, we're adding a new snapshot type we call section snapshots. And as the name implies, section snapshots encapsulates the data for a single section in a UICollectionView. There are two reasons for this enhancement-- first, to allow data sources to be more composable into section-sized chunks of data...

and second, to allow modeling of hierarchical data, which is needed to support rendering outline-style UIs, a common visual design found all throughout iOS 14. So let's go back to Emoji Explorer and see how section snapshots are used to build out this sample app. First, in our horizontally scrolling section, we see we're using a single section snapshot to completely model the content found here.

And next in our second section, where we see this expandable-collapsible outline style, a second section snapshot is used to model this hierarchical data. And finally in our list section, we again model this section's content with a third section snapshot. So for Emoji Explorer, we have composed our Diffable Data Source into three distinct section snapshots, each representing a single section's content. That's a brief overview of the new section snapshots we've added to UICollectionView's Diffable Data Source for iOS 14. But there's more. We've also added new reordering APIs. To take a deeper dive into these new APIs, please check out the video "Advances in Diffable Data Sources." Next up, let's talk about some advances in Compositional Layout for iOS 14.

Compositional Layout was introduced back in iOS 13, and it allows us to build rich, complex layouts by composing smaller, easy-to-reason bits of layout together. Compositional Layout is fast because you describe what you want the layout to look like instead of how the layout ought to work. Compositional Layout also includes the ability to have section-specific layouts to help you build more sophisticated UIs. And there's even support for orthogonal scrolling sections. To learn more about Compositional Layout, check out the WWDC 2019 video "Advances in Collection View Layout." Okay, so for iOS 14, we've built on the foundation of Compositional Layout with a new feature we call Lists.

Lists allow you to include UITableView-like sections right in to any UICollectionView.

And these lists are rich with features you've come to expect from UITableView, like swipe actions and many common cell layouts. Creating a list-style layout is simple.

Since Lists is built on top of Compositional Layout, we can easily mix and match Lists with other kinds of layout on a per-section basis. Let's check out a code snippet to see just how easy it is to create a list-styled layout with Compositional Layout.

As you can see, it's quite simple-- just two lines of code.

In this example, we're creating a UICollectionView layout where every section in our CollectionView is a list with an insetGrouped appearance.

And here's what that layout would look like.

So that's just a brief tour of Compositional Layout lists. But there's a lot more to Lists. There's a new concrete UICollectionViewListCell, header and footer support, and also a new Sidebar appearance we see in many iPadOS system apps.

For a deeper dive, please check out the video "Lists in UICollectionView." Finally, let's chat a little bit about UICollectionView and modern cells.

For iOS 14, we have a brand-new way to configure cells with a new API we call cell registrations.

Cell registrations are a simple, reusable way to set up a cell from a view model.

Cell registrations eliminate the extra step of registering a cell class or nib to associate it with a reuse identifier.

We instead use a generic registration type which incorporates a configuration closure for setting up a new cell from a view model. Let's take a look at this API in action. First, we create our cell registration, which is generic over the cell class-- in this case MyCell-- and our ViewModel class.

Notice the registration takes a closure, which is called whenever a new cell is constructed. This is where we configure the cell's content from our ViewModel. With cell registrations, we no longer need the extra step of calling register. We simply use the cell registration from our Diffable Data Source cell provider with the new API dequeueConfiguredReusableCell using registration. So that's cell registrations.

Next up, cell content configurations. Cell content configurations provide standardized layouts for cells similar to what is seen in UITableView standard cell types.

These configurations can be used with any cell, or even a generic UIView. They're very flexible. Let's check out a few visual examples to get a taste of how these work. Here we can see a simple case of an image and some text in a very standard-looking cell layout. And here's the valueCell variant, where the second text is on the trailing side of the cell.

And finally we have the subtitleCell, which has the secondary text underneath the main text.

Note here-- these content configuration types are very lightweight and simply describe what the content should look like. The framework takes care of all the layout considerations and automatically optimizes for performance.

And finally, background configurations. These are quite similar to content configurations but apply to any cell's background with the ability to adjust properties such as color, border styles and more.

So we've barely scratched the surface with modern cell configuration. For a deeper dive, please check out the video "Modern Cell Configuration." That wraps up this overview of advances in CollectionView for iOS 14. Go download the sample app to see these APIs in action. And use our code as a basis for adding these features to your apps.

And to learn more, go check out the related videos.

And thanks for watching.
