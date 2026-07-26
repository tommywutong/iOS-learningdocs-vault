---
title: Facebook Open Source 2016 year in review
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2016/12/19/android/facebook-open-source-2016-year-in-review/'
original_language: en
published: 2016-12-19
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:bd0a294db71a0390'
translated: false
---

> 原文：[Facebook Open Source 2016 year in review](https://engineering.fb.com/2016/12/19/android/facebook-open-source-2016-year-in-review/)　·　Meta Engineering — iOS

Over the past few years, Facebook’s Open Source program has grown into one of the largest and most active portfolios in the industry. In 2016, we launched 77 new projects, and our contributors made 60,000 commits. With nearly 400 projects and more than 500,000 followers across our entire portfolio, Facebook is committed to maintaining the stability and quality of our projects, and to supporting the communities that have grown around them.

![](https://engineering.fb.com/wp-content/uploads/2016/12/GPba7AAx8gLC6RYEAAAAAADpAVd3bj0JAAAD.png)

Our top projects, measured by number of total commits made this year, were all open-sourced in previous years and continue to see growth and momentum through adoption and contributions from the community.

![](https://engineering.fb.com/wp-content/uploads/2016/12/GAPb7ABjwgcg5ZMCAAAAAADrjXJzbj0JAAAB.jpg)

Though not the only sign of a project’s success, we were humbled to have two of our flagship projects, React and React Native, surpass 50,000 and 40,000 followers this year, respectively. We have three additional projects with more than 15,000 followers, three with at least 10,000 followers, and 20 projects that have reached 5,000 followers.

![](https://engineering.fb.com/wp-content/uploads/2016/12/GP7Q7QCBGVPBNZICAAAAAAAkTtoBbj0JAAAB.jpg)

We also had some notable newcomers. [Draft.js](https://engineering.fb.com/posts/1684092755205505/facebook-open-sources-rich-text-editor-framework-draft-js/), a React-based rich text editor framework, had a very popular reception within hours of being announced at the React.js Conf earlier this year. Another React-based project, [create-react-app](https://github.com/facebookincubator/create-react-app), which bundles everything you need to start building a new app into a single command-line tool, gained immediate traction and is now our fifth most popular project of all time. Create-react-app was also the first project to be launched within the [Facebook Incubator](https://github.com/facebookincubator), the new launching point that allows us to evaluate how a project is received by the community and determine how best to manage it over the long term.

![](https://engineering.fb.com/wp-content/uploads/2016/12/GEgG8ADhPDxoCYMGAAAAAAB_pIpxbj0JAAAB.jpg)

We also released a [suite](https://engineering.fb.com/posts/583946315094347/automatic-memory-leak-detection-on-ios/#) of new tools for [Android](https://engineering.fb.com/posts/998080480282805/open-sourcing-redex-making-android-apps-smaller-and-faster/) and [iOS](https://engineering.fb.com/posts/1154141864616569/building-and-managing-ios-model-objects-with-remodel/) at F8 this year, and even opened up our [F8 app](http://makeitopen.com/) to show people how they can build cross-platform apps easily with React Native and the stack of technologies that work with it. At our annual @Scale conference, we open-sourced [Zstandard](https://engineering.fb.com/posts/1658392934479273/smaller-and-faster-data-compression-with-zstandard/), a new data compression algorithm that has improved storage requirements at Facebook and beyond.

Finally, we were excited to celebrate our biggest launch — and one of the biggest in GitHub history — with [Yarn](https://engineering.fb.com/posts/1840075619545360/yarn-a-new-package-manager-for-javascript/), a new JavaScript package manager built in collaboration with Exponent, Google, and Tilde. Yarn hit 10,000 followers in its first 48 hours, and today it has more than 1,100 commits. We’re thrilled to see its usage grow, with adoption from companies like Travis CI and AppVeyor.

![](https://engineering.fb.com/wp-content/uploads/2016/12/GP3Q7QDY5z9T_IAGAAAAAAAlb3xvbj0JAAAB.jpg)

The strong interest in many of our recently launched projects all demonstrate the importance of collaboration and building tools within existing ecosystems that help address common challenges.

Our collaborations go beyond new launches. Many of the teams at Facebook work openly with others in the industry to help everyone use the projects and tools. Last April, React Native celebrated its [first open source anniversary](https://engineering.fb.com/posts/597378980427792/react-native-a-year-in-review/) with contributions from both Microsoft and Samsung, bringing React Native support to every major mobile platform. We also [worked with Spotify](http://fbinfer.com/blog/2016/03/17/collaboration-with-spotify.html) to improve the integration of Infer, our static analyzer tool, with its build system. This two-way collaboration not only helped make Infer better but also enabled many other companies, including Uber, to run Infer on their apps as well. Finally, GitHub [announced](http://githubengineering.com/the-github-graphql-api/) that it would be making its developer API available through [GraphQL](https://engineering.fb.com/posts/1691455094417024/graphql-a-data-query-language/).

![](https://engineering.fb.com/wp-content/uploads/2016/12/GBHD7ACzaQ68N8UEAAAAAADIkGUkbj0JAAAB.jpg)

In addition, we’ve continued our commitment to contribute back to projects and companies whose software we use at Facebook. We’ve contributed a host of pull requests to core [Chef](https://www.chef.io/chef/), sat on the [Chef Board of Governance](https://github.com/chef/chef-rfc/blob/master/rfc029-governance-policy.md), open-sourced 22 new [Chef cookbooks](https://engineering.fb.com/posts/1909042435988955/facebook-chef-cookbooks/), and contributed cgroup2 support to systemd. Twenty-one engineers in our kernel team made more than 600 contributions to mainline Linux, including cgroups2, MD/RAID5 caching, eBPF, btrfs, and buffered writeback fixes.

We also work closely with other teams here at Facebook to open-source a range of technologies beyond developer tools. Facebook AI Research has made many of its resources [available](https://github.com/facebookresearch) to the broader community, including [fastText](https://engineering.fb.com/posts/1438652669495149/fair-open-sources-fasttext/) — a library for text representation and classification — which became one of our top new releases this year with more than 5,000 followers. We even open-sourced a camera system: [Surround360](https://engineering.fb.com/posts/1755691291326688/introducing-facebook-surround-360-an-open-high-quality-3d-360-video-capture-system/), our 3D-360 camera, along with its state-of-the-art [stitching software](https://engineering.fb.com/posts/265413023819735/surround-360-is-now-open-source/).

It’s been a busy year, one that would not have been possible without many of you. We had 13,000 pull requests from more than 2,700 external contributors, a 40 percent increase over last year. While it’s impossible to thank everyone individually, we’d like to give a shout-out to some of our top external contributors.

![](https://engineering.fb.com/wp-content/uploads/2016/12/GN-a7ADaHO51NHkCAAAAAABVqfRybj0JAAAB.jpg)

To learn more about Facebook Open Source, visit our [open source site](https://opensource.fb.com/) or find us on [GitHub](https://github.com/facebook). See you in 2017!

![](https://engineering.fb.com/wp-content/uploads/2016/12/GO5P8wDFkS4ph5cEAAAAAAAGPpgebj0JAAAD.png)
