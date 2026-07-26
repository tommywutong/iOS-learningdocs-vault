---
title: 'React Native: A year in review'
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2016/04/13/android/react-native-a-year-in-review/'
original_language: en
published: 2016-04-13
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ab126e1889f8359a'
translated: false
---

> 原文：[React Native: A year in review](https://engineering.fb.com/2016/04/13/android/react-native-a-year-in-review/)　·　Meta Engineering — iOS

It’s been one year since we open-sourced [React Native](http://facebook.github.io/react-native/). What started as an idea with a handful of engineers is now a framework being used by product teams across Facebook and beyond. Today at F8 we announced that Microsoft is bringing [React Native to the Windows ecosystem](http://microsoft.github.io/code-push/articles/ReactNativeWindows.html), giving developers the potential to build React Native on Windows PC, Phone, and Xbox. It will also provide open source tools and services such as a React Native extension for Visual Studio Code and CodePush to help developers create React Native apps on the Windows platform. In addition, [Samsung](https://www.tizen.org/blogs) is building React Native for its hybrid platform, which will empower developers to build apps for millions of SmartTVs and mobile and wearable devices. We also released the [Facebook SDK for React Native](https://github.com/facebook/react-native-fbsdk), which makes it easier for developers to incorporate Facebook social features like Login, Sharing, App Analytics, and Graph APIs into their apps. In one year, React Native has changed the way developers build on every major platform.

It’s been an epic ride — but we are only getting started. Here is a look back at how React Native has grown and evolved since we open-sourced it a year ago, some challenges we faced along the way, and what we expect as we look ahead to the future.

## In the beginning: React Native’s roots

In the essence of Facebook’s hacker culture, React Native started as a hackathon project in the summer of 2013. Similar to [React](https://github.com/facebook/react), React Native seemed like a boldly unconventional idea. It wasn’t clear this would actually work. How was touch negotiation between JS and native ScrollViews going to work? What about performance, and what about debugging? None of these challenges stopped the engineers from focusing and pushing forward.

Once we had a working prototype, we anticipated that the project had a ton of potential for Facebook. A few years ago we made a major shift to native mobile development. However, recompiling on every code change was slow, and separate sets of skills were needed to build for iOS and Android. All of this meant slower product development. The idea of React Native meant we could bring all the things we loved about developing for the web — such as fast iterations and having a single team build the whole product — to mobile. It meant we could move faster.

As a result, we started investing time and energy into the project — we knew the only way to prove that the new technology really worked was to throw hard problems at it. We chose a News Feed prototype, which was one of the first projects we built with React Native while still developing React Native’s infrastructure. That code eventually became the basis for the feed used by the standalone Facebook Groups application.

By July 2014, there were still only a few people working on the project when React Native got its first big job: the Ads Manager team wanted to build a standalone iOS app. However, they didn’t have engineers with iOS experience. This was a perfect fit. What followed were a few months of very close collaboration between the Ads Manager product team and the React Native team. The product engineers were constantly pushing the boundaries of the platform. The goal was no smaller than to ship the first fully React Native-powered app where the user experience was identical to an app built in Objective-C.

Once we felt confident this task was possible, we made a decision to make React Native cross-platform and start a React Native Android team in London. The then team of three wrote most of the core Android runtime and first components during the second half of 2014. The goal was to run the iOS Ads Manager code on Android, and by the end of 2014 we had a bare-bones version of the app running. It was missing many views and performance wasn’t great on low-end devices, but you could see the list of ads and even create one. We were confident we could make this work so we made a push for performance and feature parity.

![](https://engineering.fb.com/wp-content/uploads/2016/04/GAtMxgCEqdsiQREEAHBX5AgAAAAAbj0JAAAB.jpg)

<sub>Facebook Ads Manager iOS codebase running on Android, January 2015.</sub>

The Facebook Ads Manager for iOS shipped in February 2015, less than six months after the team started working on it. Concurrently, everyone whose main focus was on JS or iOS worked on open-sourcing the iOS implementation. In January 2015 at React.js Conf, there was a first [public preview](https://www.youtube.com/watch?v=KVZ-P-ZI6W4), and at our F8 developer conference in March 2015, we [opened the code to everyone](https://engineering.fb.com/posts/1014532261909640/react-native-bringing-modern-web-techniques-to-mobile/).

Immediately after that, the Ads Manager product engineers started porting their JavaScript code to Android, working very closely with the React Native Android team in London. We didn’t aim for code sharing between platforms when working on the iOS Ads Manager but expected it could be a nice side effect of using React Native. When the Android Ads Manager was ready to ship, we realized that about 85 percent of the code was shared between the two apps.

In June 2015, after about three months of development and a month of internal dogfooding, the [first version of the Android Ads manager shipped](https://engineering.fb.com/posts/1189117404435352/react-native-for-android-how-we-built-the-first-cross-platform-react-native-app). Given how React Native for iOS took off, we immediately shifted our focus to open-sourcing React Native for Android, and we anticipated strong interest for the Android launch. After all, having to build the same app separately for each platform is a problem in the industry, and we knew from experience with the Ads Manager that React Native could help with it.

Similar to the iOS launch, we wanted to get React Native for Android out as early as possible to get feedback. Therefore, we started with only the core runtime and small number of view and modules (Text, Image, ScrollView, Network, AsyncStorage, and a few others). On September 14, we pushed the core of the Android runtime and an initial set of Android modules to GitHub and npm. And just like that, React Native version 0.11 was the first release with Android support. We’ve added the following Android modules since we open-sourced it, bringing the API parity close to iOS: Alert, AppState, CameraRoll, Clipboard, Date and time pickers, Geolocation, Intent, Modal, NetInfo, Pull to refresh view, Picker, Slider, View Pager, and WebView.

Needless to say, the adoption that followed outside of Facebook has made all of us on the React Native team extremely excited.

![](https://engineering.fb.com/wp-content/uploads/2016/04/GHD6twDweJdl_ZkEAIh72gEAAAAAbj0JAAAB.jpg)

<sub>Timeline of the progress since the inception of React Native until open-sourcing React Native for Android.</sub>

## Rapid adoption: A year of learning and growth

The adoption of React Native and its developer community have both grown much faster than we had expected.

Over 650 people have committed code to the React Native codebase. Out of the 5,800 commits to the codebase, 30 percent were made by contributors who don’t work at Facebook. In February 2016, for the first time, more than 50 percent of the commits came from external contributors. With so many people from the community contributing to React Native, we’ve seen as many as 266 new pull requests per month (up to 10 pull requests per day). Many of these are high-quality and implement widely used features.

![](https://engineering.fb.com/wp-content/uploads/2016/04/GDr6twAKUI1CVKQDAOLoKBAAAAAAbj0JAAAB.jpg)

<sub>Number of pull requests opened on the React Native GitHub repo each month.</sub>

In the beginning, the number of incoming pull requests made it difficult to review them quickly and efficiently. Finding the right reviewers for each pull request meant lots of manual work every day. To solve this, we automated everything that we could by building two GitHub bots.

The first was the mention bot, which finds the right reviewers for each pull request.

![](https://engineering.fb.com/wp-content/uploads/2016/04/GPNLxgD6IVtWtN4DAA9XT2YAAAAAbj0JAAAB.jpg)

<sub>The mention bot finds the best reviewers for a pull request based on blame information.</sub>

The [mention bot](https://github.com/facebook/mention-bot), which is now open-sourced, helped streamline how many pull requests we could review each day. An interesting fact is that with over 50 percent of the commits last month contributed by the community, the bot often identifies people in the community as best reviewers.

The second problem we had was that merging pull requests wasn’t easy enough. Facebook engineers use the exact same React Native code you see on GitHub; we don’t have a fork of the codebase. Therefore, we automatically test apps like the Facebook Ads Manager before merging your pull request to our large Mercurial repo called [fbsource](https://www.facebook.com/FacebookforDevelopers/videos/10152800517193553/).

![](https://engineering.fb.com/wp-content/uploads/2016/04/GOJLxgBXEyGtXcEBAOk431UAAAAAbj0JAAAB.jpg)

<sub>Simplified structure of our monolithic Mercurial repo called fbsource. The repo contains all our mobile and backend code.</sub>

The process of merging a pull request used to involve several manual steps. We simplified all of this to typing a single comment on GitHub.

![](https://engineering.fb.com/wp-content/uploads/2016/04/GBtMxgBxO5-K-scAAPg6JBUAAAAAbj0JAAAB.jpg)

<sub>@facebook-github-bot shipit: If all internal tests pass, the code is merged to fbsource master as well as GitHub master.</sub>

Thanks to these tools, the project has been able to keep up with the very large number of incoming pull requests. In total, 2,351 pull requests have been closed in just a year.

![](https://engineering.fb.com/wp-content/uploads/2016/04/GOFLxgD6zKrjWJQEAHg8yjsAAAAAbj0JAAAB.jpg)

<sub>The number of open pull requests closed each month.</sub>

### Managing GitHub issues

The popularity of the project has created an environment where there is a lot of potential impact to be had by anyone who wants to help us manage the massive number of issues that are opened.

We have implemented another bot to help anyone manage GitHub issues. It makes it possible for anyone to close issues as duplicates, close them as answered, add labels, and much more. There is also a [guide to managing GitHub issues](https://github.com/facebook/react-native/blob/master/docs/IssueGuidelines.md) that you can use.

![](https://engineering.fb.com/wp-content/uploads/2016/04/GAhMxgCQLsssW78DAM1gGVkAAAAAbj0JAAAB.jpg)

<sub>The issues bot lets anyone manage GitHub issues, no push access needed.</sub>

The API surface area of React Native is huge. It exposes most of the building blocks of iOS and Android apps to JavaScript, while adding cross-platform abstractions. It would be challenging for any single person to be closely familiar with all the APIs. Even though many product teams at Facebook use React Native, we will not always hit all the edge cases before you do. React Native is working for us, but we can’t perfect it alone. This is why having a community that’s familiar with the codebase is important not only to us but also to others involved in the broader ecosystem, who rely on it for the success of their app, service, or third-party module.

### Community collaborators

React Native Open Source Collaborators are people in the community who contribute very high-quality patches and actively help others. We have created the React Native Community Collaborator title for people who greatly help us move the project forward. With the title comes push access to the repo.

Here is a big shout-out to the React Native community collaborators: [Adam Miskiewicz](https://twitter.com/skevy), [Alexey Kureev](https://twitter.com/kureevalexey), [Brent Vatne](https://twitter.com/notbrent), [Chirag Jain](https://twitter.com/jain_chirag04), [Christopher Dro](https://twitter.com/_cdro), [James Ide](https://twitter.com/ji), [Janic Duplessis](https://github.com/janicduplessis), [Joshua Sierles](https://twitter.com/jsierles), [Kyle Corbitt](https://twitter.com/corbtt), [Krzysztof Magiera](https://twitter.com/kzzzf), [Leland Richardson](https://twitter.com/intelligibabble), [Mike Grabowski](https://twitter.com/grabbou), and [Satyajit Sahoo](https://twitter.com/satya164). Thank you for all your amazing work!

Some of us met at React.js Conf in San Francisco on Feb. 22, 2016:

![](https://engineering.fb.com/wp-content/uploads/2016/04/GP5LxgAlbXcaFAcDALF7qnsAAAAAbj0JAAAB.jpg)

<sub>In the picture (left to right): Christopher Dro (React Native Playground), Brent Vatne (Exponent), Jean-Richard Lai (TaskRabbit), Eric Vlad Vicenti (React Native team), Dave Sibiski (React Native Playground), James Ide (Exponent), Martín Bigio (React Native team), Tadeu Zagallo (React Native team), Christopher Chedeau (React Native team), Ken Wheeler (Formidable), Leland Richardson (Airbnb), and Martin Konicek (React Native Team).</sub>

## React Native today

There is a new release of React Native every two weeks. This is so that you can get the latest features quickly after they land in master. The code was downloaded about 70,000 times from npm in March 2016. With more than 30,000 stars, React Native is the 21st most starred repo on GitHub.

![](https://engineering.fb.com/wp-content/uploads/2016/04/GPRLxgBggDVEBxwGAN2kKw8AAAAAbj0JAAAB.jpg)

<sub>The number of stars on the GitHub repo went from zero to almost 30,000 in just year.</sub>

### What the community has done with React Native

In the year since the iOS launch, there have been quite a few apps released to the App Store, and high-quality Android apps are starting to appear too. The [Showcase](https://facebook.github.io/react-native/showcase.html) on the website lists 107 apps created using React Native. Add yours by sending a [pull request](https://github.com/facebook/react-native/blob/master/website/src/react-native/showcase.js).

[![](https://engineering.fb.com/wp-content/uploads/2016/04/12765871_1793294967565463_1123475056_n.jpg?w=580&h=326&crop=1)](https://engineering.fb.com/2016/04/13/android/react-native-a-year-in-review/attachment/12765871_1793294967565463_1123475056_n/)

<sub>Running is a run tracker that’s just beautiful. It was one of the early React Native apps with amazing design.</sub>

[![](https://engineering.fb.com/wp-content/uploads/2016/04/12995561_2040283936196697_182137555_n.jpg?w=580&h=326&crop=1)](https://engineering.fb.com/2016/04/13/android/react-native-a-year-in-review/attachment/12995561_2040283936196697_182137555_n/)

<sub>Townske is a city guides app that was featured in the Best New Apps section on the App Store.</sub>

[![](https://engineering.fb.com/wp-content/uploads/2016/04/12995598_886158228160054_2007991858_n.jpg?w=580&h=326&crop=1)](https://engineering.fb.com/2016/04/13/android/react-native-a-year-in-review/attachment/12995598_886158228160054_2007991858_n/)

<sub>Discovery VR lets you explore Discovery Channels’ 360 videos. This was the first VR app built with React Native.</sub>

[![](https://engineering.fb.com/wp-content/uploads/2016/04/12995600_1999294613629759_1901772811_n.jpg?w=580&h=326&crop=1)](https://engineering.fb.com/2016/04/13/android/react-native-a-year-in-review/attachment/12995600_1999294613629759_1901772811_n/)

<sub>Some of the most well-crafted React Native apps that we have come across. Be sure to check them out to get a feel for what React Native is capable of!</sub>

There are many more high-quality apps than can fit into a blog post. Check out the Showcase to see all the apps we know about.

Beyond apps, there is a wide variety of services that build upon or complement React Native: [Exponent](https://exponentjs.com/) lets you build and share React Native apps without having to compile anything; [React Native Playground](https://rnplay.org/) lets you edit and run React Native apps in the browser; [AppHub](https://apphub.io/) and [Microsoft CodePush](https://microsoft.github.io/code-push/) let you deploy code instantly without going through the app stores; [JS.coach](https://js.coach/react-native) is a database of third-party modules; and [Deco](https://www.decosoftware.com/) is an IDE for React Native.

There is a growing ecosystem of third-party modules that you can simply plug into your apps. Thanks to JS.coach, the modules are easily searchable, and thanks to [rnpm](https://github.com/rnpm/rnpm), installing them is easy.

There have been an incredible number of blog posts and tutorials written about React Native. Thank you for all of them, and keep them coming! We’ll highlight Brent Vatne’s [React Native Newsletter](http://brentvatne.ca/react-native-newsletter/), which is a great overview of everything happening around React Native and has links to many of the great blog posts.

Did we mention three [books](http://www.reactnative.com/books/) have been written about React Native?

Overall, a lot has happened in just one year!

### React Native at Facebook

More and more product teams at Facebook have been building new features and apps with React Native. It’s being used in standalone apps and in the main Facebook app on iOS and Android.

![](https://engineering.fb.com/wp-content/uploads/2016/04/GNhLxgCphPP1TugAAL4rED4AAAAAbj0JAAAB.jpg)

<sub>The Facebook Groups app is a hybrid app where the feed is powered by React Native.</sub>

The React Native team has grown from around 10 to around 20 engineers in the past year and has strong representation in [Menlo Park](https://www.facebook.com/careers/locations/menlo-park/), [London](https://www.facebook.com/careers/locations/london/), and [New York](https://www.facebook.com/careers/locations/newyork/). The main focus areas of the React Native team since the Ads Manager launch have been the following:

- Improving performance such as startup time, responsiveness, and scroll performance. See the [blog post on React Native performance](https://engineering.fb.com/posts/895897210527114/dive-into-react-native-performance/) and a note on [scheduling](https://www.facebook.com/notes/andy-street/react-native-scheduling/10153916310914590).
- Integrating with UI and infrastructure of the main Facebook app, both on iOS and Android
- Building performance tooling such as CPU and memory profilers
- Building new features needed by product teams at Facebook
- Supporting product teams by answering questions and fixing bugs quickly
- Developer experience, such as integrating with internal developer tools and build systems

## Looking ahead

The project has picked up incredible traction in the last year, and, as we like to say at Facebook, we are 1 percent finished. We will continue investing in the project internally. During the last year, the team size has doubled. We will also continue investing in open source tooling. We want React Native to be a successful project both at and outside of Facebook.

Here are a few of the best ways to get involved in the project:

- If you find a bug, please send a fix. Small pull requests with a Test Plan are the quickest to get reviewed.
- If you find anything in the documentation unclear, please improve the docs by sending a pull request.
- Ask and answer questions on [StackOverflow](http://stackoverflow.com/questions/tagged/react-native).
- Help others with GitHub issues.
- If you would like to propose a new feature, the best way is to post it on [Product Pains](https://productpains.com/product/react-native/?tab=top), which has a voting system. If you don’t have time to implement it yourself, it might still get upvoted enough that others will implement it.
- Join the [React Native Community](https://www.facebook.com/groups/react.native.community/) group on Facebook.

If you’re new to React Native, we’ve built a series of [tutorials](http://makeitopen.com/) designed to introduce the framework and its open source ecosystem. Using this year’s [F8 app](https://github.com/fbsamples/f8app/) as an example, we show how to design an app for multiple platforms, integrate data, and test the app to improve your code as you’re writing it.

Thank you to everyone who’s built amazing apps with React Native, built tools and services on top of React Native, wrote third-party modules, helped answer questions, submitted pull requests, organized conferences, and blogged about React Native — keep doing all of that!

Here’s to the next year!
