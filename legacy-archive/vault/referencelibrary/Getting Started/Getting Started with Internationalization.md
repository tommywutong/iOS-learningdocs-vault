---
title: Getting Started with Internationalization
apple_id: TP30001113
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_Internationalization/_index.html
archived_at: '2026-07-18T02:39:24.240676Z'
---
> 导航：[总目录](../../README.md) · [referencelibrary](../../_indexes/referencelibrary.md)



## Introduction

### Technology Overview

The size of the global market for your software application depends on its support for locale-specific content and functionality. Designing an application with the world in mind, a process known as _internationalization_, makes it easier and less costly to adapt it to other cultures or regions. The adaptation process, often performed simultaneously for several target markets, is known as _localization_.

The best time to internationalize is during product development. Not only will you shorten your time to foreign markets; following internationalization principles will often help to create a more solid native-language product that is easier to maintain and revise. Legacy applications can be fully internationalized as well.

### Start Here

If you’ve never internationalized a product, become familiar with the process by reading:

- The [ADC Topic Page for Internationalization](https://developer.apple.com/internationalization/) for links to Apple’s internationalization resources
- [Introduction to i18n](http://www.debian.org/doc/manuals/intro-i18n/) (from the open-source Debian software project) to get a grounding in the concepts important to internationalization
- The [Terminology](http://www.gala-global.org/terminology.html) pages from the Globalization and Localization Association for a comprehensive glossary of internationalization terms
- [Internationalization and Localization Guide](../../documentation/Mac%20OSX/Internationalization%20and%20Localization%20Guide/About%20Internationalization%20and%20Localization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2i) to learn how Mac OS X arranges and uses localized resources for an application
- [Internationalization and Localization (PDF)](https://developer.apple.com/pdf/mactech_intl.pdf) to understand the costs and benefits of internationalizing your product

### Choose a Learning Path

If you’re bringing an internationalized application to Mac OS X from a Windows or UNIX platform, you’ll want to learn about porting issues. If you’re starting a new project, or retrofitting an old one, you’ll want a deeper understanding of location independence and how to apply it. If your application works with text, you’ll want to learn about Unicode in Mac OS X.

#### Porting an Internationalized Application

If you have an existing, internationalized application developed for a Windows or UNIX platform, you’ll want to know about differences you’ll encounter upon moving your code to Mac OS X.

- __If you are bringing an internationalized application from Windows to Mac OS X__, read [Internationalization](https://developer.apple.com/library/archive/documentation/Porting/Conceptual/win32porting/Articles/intern.html#//apple_ref/doc/uid/20002357) in [Porting to Mac OS X from Windows Win32 API](../../documentation/Porting/Porting%20to%20Mac%20OS%20X%20from%20Windows%20Win32%20API/Porting%20to%20Mac%20OS%20X%20from%20Windows%20Win32%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4ta2i).
- __If you are bringing an internationalized open source application to Mac OS X__, review [Internationalization](http://icu-project.org/userguide/i18n.html) in [User Guide](http://icu-project.org/userguide/) for the International Components for Unicode (ICU). Read [UNIX Porting Guide](https://developer.apple.com/documentation/Porting/Conceptual/PortingUnix/).

#### Designing for Location Independence

Your application should not assume that a user is in any particular location in the world with regard to their expectations for address formats, measurement systems, currency symbols, writing direction, or colors. Build your application from the ground up for location independence to maximize its localizability.

- __To gain a deeper understanding of locales and how they are implemented in Mac OS X__, read [Locales Programming Guide](../../documentation/Core%20Foundation/Locales%20Programming%20Guide/Introduction%20to%20Locales.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4dc2i).
- __Whether developing a Carbon or Cocoa application__, read Worldwide Compatibility in Apple Human Interface Guidelines.
- __If you are designing or retrofitting a Carbon application for location independence__, read [Preferences Programming Topics for Core Foundation](../../documentation/Core%20Foundation/Preferences%20Programming%20Topics%20for%20Core%20Foundation/Introduction%20to%20Preferences%20Programming%20Topics%20for%20Core%20Foundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezds2i). Also read Introduction to International Text on the Mac OS and Overview of Text Handling in [Handling Unicode Text Editing With MLTE](../../documentation/Carbon/Handling%20Unicode%20Text%20Editing%20With%20MLTE/MLTE%20Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobt).
- __If you are designing or retrofitting a Cocoa application for location independence__, read [Internationalization and Localization Guide](../../documentation/Mac%20OSX/Internationalization%20and%20Localization%20Guide/About%20Internationalization%20and%20Localization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2i) and [Preferences and Settings Programming Guide](../../documentation/Cocoa/Preferences%20and%20Settings%20Programming%20Guide/About%20Preferences%20and%20Settings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2ts2i).

#### Adding Unicode Support

Unicode is the native text file encoding for Mac OS X, a feature that streamlines your internationalization effort. But there are a variety of considerations to keep in mind depending on your application and your development strategy.

- __If your Mac OS X application works with text__, read File Encodings and Fonts in [Internationalization and Localization Guide](../../documentation/Mac%20OSX/Internationalization%20and%20Localization%20Guide/About%20Internationalization%20and%20Localization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2i).
- __If you are developing using Carbon__, read [Handling Unicode Text Editing With MLTE](../../documentation/Carbon/Handling%20Unicode%20Text%20Editing%20With%20MLTE/MLTE%20Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobt), [Multilingual Text Engine Frequently Asked Questions](https://developer.apple.com/technotes/tn/tn2026.html), [ATSUI Programming Guide](../../documentation/Carbon/ATSUI%20Programming%20Guide/Introduction%20to%20ATSUI%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobu), and [Supporting Unicode Input](https://developer.apple.com/documentation/Carbon/Conceptual/Supporting_Unicode_Input/).
- __If you are developing using Cocoa__, read Text System Architecture.

### Next Steps

The [Internationalization Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30001073) includes the following high-level resource pages, which can be bookmarked for easy access:

- [Guides](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000440-TP30000421-TP30001072)

  Conceptual and how-to information for internationalization.
- [Reference](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000421-TP30001072)

  Focused, detailed descriptions in reference format for internationalization in Carbon, Cocoa, and Core Foundation.
- [Release Notes](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000872-TP30001073)

  Notes containing the latest news about Mac OS X features affecting internationalization.
- [Sample Code](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000925-TP30001073)

  Sample applications demonstrating internationalization techniques.
- [Technical Notes](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000924-TP30001073)

  Late-breaking information on issues related to Internationalization.
- [Technical Q&As](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000926-TP30001073)

  Programming tips, code snippets, and FAQs by Apple’s support engineers.
- Mailing Lists

  The [carbon-development](http://lists.apple.com/mailman/listinfo/carbon-development) and [cocoa-dev](http://lists.apple.com/mailman/listinfo/cocoa-dev) mailing lists include discussions of internationalization topics among Mac OS X developers.

These additional internationalization resource pages may also be helpful:

- Apple’s [Regional Information](https://developer.apple.com/regions/)

  Global marketing and business information for Mac OS X.
- [Unicode Consortium](http://www.unicode.org/)

  Publishers of the Unicode standard.
- [Localization Industry Standards Association](http://www.lisa.org/)

  An international association for the globalization, internationalization, localization, and translation industries.

