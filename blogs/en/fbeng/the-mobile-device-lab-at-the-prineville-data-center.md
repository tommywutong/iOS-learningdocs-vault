---
title: The mobile device lab at the Prineville data center
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2016/07/13/android/the-mobile-device-lab-at-the-prineville-data-center/'
original_language: en
published: 2016-07-13
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:365dd99f9f5ad107'
translated: false
---

> 原文：[The mobile device lab at the Prineville data center](https://engineering.fb.com/2016/07/13/android/the-mobile-device-lab-at-the-prineville-data-center/)　·　Meta Engineering — iOS

As more people around the world come online for the first time, we want to make sure our apps and services work well for everyone. This means we need to understand the performance implications of a code change on both high-end and typical devices, as well as on a variety of operating systems. We have thousands of changes each week, and given the code intricacies of the Facebook app, we could inadvertently introduce regressions that take up more data, memory, or battery usage.

Last year we developed [CT-Scan](https://engineering.fb.com/posts/924676474230092/mobile-performance-tooling-infrastructure-at-facebook/), a service that helped us understand the performance implications of code changes and decrease the number of software regressions. When a commit lands in a repository, CT-Scan performs a build and runs performance tests, such as cold and warm start, feed scroll performance, and battery consumption. The results are plotted and engineers can learn whether they're causing an issue with a new build.

Initially, engineers tested code by running CT-Scan on a single device that they had at their desks. This didn't scale — we needed to be able to run tests on more than 2,000 mobile devices to account for all the combinations of device hardware, operating systems, and network connections that people use to connect on Facebook. Today, in our Prineville data center, we have a mobile device lab — outfitted with a custom-built rack — that allows us to run tests on thousands of phones. The process of building a lab in our data center wasn't a direct path, and we learned a lot along the way as we worked to scale out the promise of CT-Scan.

## The journey to a data center

To do this, we formed a small team within the [Production Engineering](http://code.facebook.com/pe) organization. The first step was to choose whether we'd use a simulator or continue with on-device testing. Simulators can help us find out whether the app behaves correctly, but they're not well-suited to test the performance of the app. For example, we wouldn't be able to track down a 1 percent performance regression in a simulator. So we opted for on-device testing.

Our first setup was “the sled.” On the sled, phones were placed on a metal rack, which slid into a metal case. When you slide a bunch of metal sleds into a metal rack, you end up with too much metal, and we lost all Wi-Fi.

![](https://engineering.fb.com/wp-content/uploads/2016/07/GNEj0ACOS0-NukoCAIpxZywAAAAAbj0JAAAB.jpg)

<sub>The sled.</sub>

Our second version was named “the gondola” and allowed us to deploy 100 devices for testing. The gondola was a plastic rack — which didn't interfere with the Wi-Fi — but the short length of the USB cables caused a lot of issues. The gondola was a tangled mess.

![](https://engineering.fb.com/wp-content/uploads/2016/07/GNIj0ABUuPcitI8FAPRW3y4AAAAAbj0JAAAB.jpg)

<sub>The gondola.</sub>

Next up, we built “the slatwall.” The slatwall took up an entire room, and we were able to deploy 240 devices. To accommodate 2,000 phones (our target number based on several factors, including the number of commits per week, the number of iterations needed per test to get statistically significant results, etc.), we'd need to scale to nine of these rooms in our Menlo Park headquarters within a year. This wouldn't work, so we decided to move our mobile device lab into a data center.

![](https://engineering.fb.com/wp-content/uploads/2016/07/GJ9e0ADUTQGU7F0AACqkrhgAAAAAbj0JAAAB.jpg)

<sub>The slatwall.</sub>

### Hardware: The mobile rack

One of the first issues we tackled when transitioning into a data center was creating a consistent environment for running tests. If we were to use the same racks for mobile device testing that we use for our servers in our data center, our tests would be unsuccessful because the Wi-Fi signal from one rack would interfere with the Wi-Fi signal from the next rack. We needed racks to be well-isolated from their neighbors — ensuring a consistent environment — in order for our tests to be reliable and to have reproducible results.

We custom-built our own racks, designing them to function as an electromagnetic isolation (EMI) chamber. Each rack holds eight Mac Minis (or four [OCP Leopard servers](http://www.opencompute.org/wiki/Server/SpecsAndDesigns) for Android testing) that drive the phones to install, test, and uninstall the application we're testing. Each Mac Mini is connected to four iPhones, and each OCP Leopard server is connected to eight Android devices, for a total of 32 phones per rack. The phones connect to Wi-Fi via a wireless access point in each rack. These phones lie on a slightly tilted pegboard so mounted cameras can record their screens. Engineers can access these cameras remotely to learn more about how each phone reacts to a code change.

We ran into two major challenges when building the rack. The first was that we needed consistent throughput inside the rack. We thought the proximity of the phones to one another would create problems, and we were unsure whether the wireless access point (WAP) could drive all the phones. So we tested. We discovered that we could drive up to 64 phones with one WAP and still reach a throughput of 500 kbps per phone. However, we also knew the mobile phones would need a 4-foot air gap from the WAP in order to have sufficient attenuation of the signal when it reaches them; if not, the signal hitting the phones would be too strong and we wouldn't get optimal performance. We also knew we'd have scaling issues with one Mac Mini supporting more than four iPhones at a time. So eight Mac Minis per rack supporting four phones each led us to settling on 32 total phones per rack.

The second challenge was that we needed to minimize interference across the racks by containing the Wi-Fi signal to only one rack. In theory, we needed an attenuation of 100 dB between two racks in order for the phones not to pick up the Wi-Fi of the neighboring rack. When we tested our EMI enclosure, we found that it was about as efficient at blocking radio signal as a sieve is at blocking water.

To turn our sieve into a bucket, we took the following steps:

1. Grounded the EMI enclosure by connecting it to one of the metallic surfaces of the rack itself.
2. Covered the inside seams with copper tape.
3. Added insulation foam inside the rack.
4. Added a 100 dBm power filter (i.e., a filter for power, USB, and ethernet that's rated to filter out electromagnetic radiation and to ensure that it doesn't interfere with the Wi-Fi signal inside the enclosure).
5. Added even more insulation foam.

With this configuration, we achieved a signal attenuation of 122 dB from one rack to the next.

![](https://engineering.fb.com/wp-content/uploads/2016/07/GD6e0AAZ8YQ23GAGAF7EHz0AAAAAbj0JAAAB.jpg)

<sub>We're working to open-source the designs of this custom-built rack.</sub>

### Software challenges

Scaling our mobile device testing also involved software challenges. We needed to create a way to monitor the phones, create alerts to signal abnormal conditions, and then remediate or alert the Site Ops team at the data center to manually fix the issue. So we introduced package management and [Chef](https://www.chef.io/), a tool for managing the configuration of a server. (For example, Chef manages which software packages need to be installed, which services need to be running, what the configuration files for a service should look like, how to notify the service when those configurations change, and more.)

Prior to the Production Engineering team getting involved, hosts were hand-configured. Each host had a slightly different configuration, and things would break on one host and work on another, making it hard to understand problems. Package management gives us control over the versions of each tool we deploy and ensures that we have the same version on every host. This eliminates failures due to a particular package version being on one host and not another.

Chef allows us to define a configuration for the hosts and makes sure each host is in this specific state. Eliminating manual configuration led to uniformity across all our hosts. Together, package management and Chef removed the host as a source of problems and gave us more confidence that the device was the problem — making us more efficient when it came to implementing fixes.

We realized that most of what we were already doing in Python for managing the state of the phones was reinventing a configuration management system. Since Chef is the tool we use for that purpose on the server side, and most engineers are familiar with it, we also decided to use Chef to inspect and manage the configuration for the mobile devices.

Our Chef recipes check that the phone is in the right state. If it's not and can be modified by Chef, it's automatically fixed. If it can't be modified, the Chef run fails, and the output is logged in a centralized system and reviewed by automated tools. We created alarms on certain Chef failures, which allows us to have a dashboard of the most common failures and to create tickets for our on-site tech support team, if needed. We aim to open-source these Chef recipes in the future, so others can benefit.

## The future

Today we have around 60 racks for mobile device testing in our Prineville data center. As we continue to scale the lab, we're working to densify the current rack design to hold up to 64 phones per rack, versus 32. There are multiple challenges we're working through here.

On the Android racks, we have servers that need an in-memory check out of the repository (one per device). We already know that for this to work for 16 devices — our target if we don't want to change the server layout — we'll have to find a new solution for in-memory checkout. Our hope is to be able to get rid of the repositories on those servers entirely.

For all devices, we have to maintain a 4-foot air gap between the phones and the antenna for the signal to be sufficiently attenuated once it reaches the phones. We don't have a lot of space to stack the phones if we want to have two shelves instead of one. Additionally, we intend to get larger form-factor phones in the rack next year, which we will need to consider in the redesign.

We also need to extend Chef for mobile phones to better support iOS. For example, we'd like to be able to completely configure a device or install and remove applications from the phone. Reliably running tests on iOS devices currently involves a 20-step manual procedure to configure the phone and get it in the appropriate state. We want to reduce this to a single manual step, which is to accept the trust dialog.

We're also working to make the mobile lab capable of serving the needs of more teams across Facebook by providing a generic platform usable by any team that wants to do on-device testing. Today, the production engineering team serves only engineers who write tests using CT-Scan's framework. Some teams have use cases that don't fit well with CT-Scan's model, and we want to support those cases. To achieve this, we're collaborating on a product called [WebDriver](https://www.w3.org/TR/webdriver/), which allows us to describe a test in a standard way and then run it on a device while collecting metrics and screen output.

The tools we build for our lab support hundreds of thousands of continuous experiments and thousands of diagnostic and profiling runs. More important, they ensure that our code doesn't have performance implications for people who use Facebook. We hope that through our open-sourcing both the hardware design of our mobile device testing rack and the Chef recipes written to control the phones, others can benefit from our learnings and contribute their own ideas to our designs.

![](https://engineering.fb.com/wp-content/uploads/2016/07/GM280AACQEaTWZoEAB7CDmMAAAAAbj0JAAAB.jpg)

<sub>The mobile device lab at Prineville.</sub>
