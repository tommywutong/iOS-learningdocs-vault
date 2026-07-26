---
title: 'Emerge Tools Blog | The Emerge CLI'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/the-emerge-cli'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:b3778daf15c5e32d'
translated: false
---

> 原文：[Emerge Tools Blog | The Emerge CLI](https://www.emergetools.com/blog/posts/the-emerge-cli)　·　Emerge Tools Blog

# The Emerge CLI

February 10, 2025 by

Trevor Elkins & Itay Brenner

CLI

![The Emerge CLI](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcover.c776cf2c.png&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

## The Emerge CLI

If you've read our previous blog post about [Bring Your Own Snapshots](https://www.emergetools.com/blog/posts/bring-your-own-snapshots), you might have noticed that we now have an official CLI for Emerge! This is long overdue and we have many exciting features planned to make Emerge easier to use.

Our CLI is distributed as a Ruby Gem. To get started, you can install the CLI using the following command:

```shell
gem install emerge
```

And once installed, you can run the help command to see what's available:

```shell
emerge --help
```

## [Our vision](https://www.emergetools.com/blog/posts/the-emerge-cli#our-vision)

Much of our existing tooling is geared towards CI integration, whether through our Fastlane and Gradle plugins or manually calling the API. A typical CI flow involves building your app and then uploading it to Emerge. Then, we analyze the app and report results back to the originating pull request.

Part of the CLI's functionality will be geared towards making the Emerge integration easier. But the CLI also addresses a current limitation of Emerge: we can only see what's included in your upload.

Emerge analyzes the compiled result of an app, meaning we have limited knowledge of the source code. We can suggest insights to fix for the app, but we rely on the developer to implement the fixes. And we can't suggest fixes tailored to the codebase itself, only generalized suggestions that won't work for every project.

Now, with a CLI, we can finally get the best of both worlds and do much more. Our vision is to make using Emerge as easy as possible, and also provide commands that an everyday mobile developer can find useful.

## [Current functionality](https://www.emergetools.com/blog/posts/the-emerge-cli#current-functionality)

### [Snapshot Testing: BYO Snapshots](https://www.emergetools.com/blog/posts/the-emerge-cli#bring-your-own-snapshots)

Our Snapshots product is used everyday by companies like [OpenAI](https://www.emergetools.com/blog/posts/openai-on-mobile-development-previews-and-snapshot-testing) and we wanted to expand it to support more use-cases and libraries. With the CLI, you can upload snapshot tests from popular libraries like Paparazzi, Roborazzi, or swift-snapshot-testing snapshots to take advantage of Emerge's infrastructure and UI.

For example, in our Hacker News app, [supporting swift-snapshot-testing](https://github.com/EmergeTools/hackernews/blob/main/.github/workflows/ios_emerge_upload_snapshots.yml#L83) is as easy as:

```shell
emerge upload snapshots \
--name "HackerNews Swift-Snapshot-Testing" \
--id "com.emerge.hn.Hacker-News.swiftsnapshottesting" \
--repo-name "EmergeTools/hackernews" \
--client-library swift-snapshot-testing \
--project-root .
```

Check out the [full docs](https://docs.emergetools.com/docs/bring-your-own) and [announcement post](https://www.emergetools.com/blog/posts/bring-your-own-snapshots) to give it a try!

### [Deleting Unused Code: Reaper](https://www.emergetools.com/blog/posts/the-emerge-cli#reaper)

Reaper allows teams like [Duolingo](https://blog.duolingo.com/emerge-tools-reaper/) to detect unused code in their apps using runtime analysis. Once you detect unused code you often want to delete it, but our users consistently report that this process involves a lot of back and forth between looking at our report and finding the files in your project.

![Example of a Duolingo Reaper report](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog33%2Fduolingo-reaper.png&w=1200&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Example of a Duolingo Reaper report

This is a perfect use-case where our CLI can help make this easier. Now you can load the Reaper report locally:

```shell
emerge reaper --id 57f13c92-30ae-4b93-98cf-3bb4bba3b
```

And then interactively delete code from your project. It's easier than ever to write code so it should be easier than ever to intelligently delete it.

### [Build Distribution](https://www.emergetools.com/blog/posts/the-emerge-cli#build-distribution)

Our newest product, Build Distribution, lets you download test builds for your app. Naturally, downloading the build is only one part of the equation, you still need to install it on the target device. Our CLI can take care of both:

```shell
emerge install build --id 9c1dec32-e5a0-4c11-a2e1-fc9a4007fb32
```

### And more

This is just a sneak peak of what we have. Our full list of commands can be seen by running `emerge --help`:

```shell
Commands:
emerge autofix [SUBCOMMAND]
emerge build-distribution [SUBCOMMAND]
emerge configure [SUBCOMMAND]
emerge integrate [SUBCOMMAND]
emerge order-files [SUBCOMMAND]
emerge reaper
emerge snapshots [SUBCOMMAND]
emerge upload [SUBCOMMAND]
```

## Contributing

Our CLI is open-source and available on [GitHub](https://github.com/EmergeTools/emerge-cli). We welcome any contributions and feedback to the project. This is just the beginning for the Emerge CLI and we have many exciting plans ahead.
