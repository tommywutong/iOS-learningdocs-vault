---
title: 'Home Lab: The Accidental System I didn’t set out to build a home lab, but one emerged anyway. This post shares the choices I made to solve one-off problems and how those choices accumulated into a sur'
source: Always Processing (Brian T. Kelley)
source_key: alwaysprocessing
source_url: 'https://alwaysprocessing.blog/2023/06/11/hl-accidental-system'
original_language: en
published: 2023-06-11
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:6a89da59c7154bf4'
translated: false
---

> 原文：[Home Lab: The Accidental System I didn’t set out to build a home lab, but one emerged anyway. This post shares the choices I made to solve one-off problems and how those choices accumulated into a sur](https://alwaysprocessing.blog/2023/06/11/hl-accidental-system)　·　Always Processing (Brian T. Kelley)

# Home Lab: The Accidental System

![A scene of old computers and peripherals haphazardly arranged to be somewhat usable.](https://alwaysprocessing.blog/cdn-cgi/imagedelivery/WFfM6PwcxpVzRRpdvDWNtg/c3fa418f-255e-4235-2204-295939a90300/public)

I didn’t set out to build a home lab, but one emerged anyway. This post shares the choices I made to solve one-off problems and how those choices accumulated into a surprisingly large collection of hardware and services.

Over the years, I accumulated various systems, devices, and services in responding to an immediate need. However, I didn’t have a holistic, coherent plan, and the responsive, ad hoc approach created unnecessary churn, especially for the WiFi hardware. In the following sections, I’ll describe each notable investment and its motivating event, organized chronologically, to show how I accidentally stumbled into building a [home lab](https://www.reddit.com/r/homelab/wiki/introduction/).

## Evolution of the Home Lab

### Network, Version 1

I moved into a new townhouse in September 2014 and brought the only infra I had at the time: an AirPort Extreme[[1](#_footnotedef_1)]. I installed it in the [wiring enclosure](https://www.legrand.us/audio-visual/structured-wiring-enclosures/metal-enclosures/28-inch-enclosure-with-hinged-door/p/en2850) on the third floor, which kept it and the cable modem out of sight. However, the install location (at the end of both the horizontal and vertical footprints of the home) and placement (in a metal box) are both sub-optimal choices for whole-house coverage, so I added a wired [AirPort Express 802.11n (2nd Generation)](https://support.apple.com/kb/SP651?locale=en_US) access point on the first floor.

I didn’t have many leaf nodes in my network topology at the time (a phone, a laptop, a work laptop, an Apple TV, and probably a few others), so this setup worked well enough for a few years. (I don’t consider the leaf nodes part of the home lab, so I’ll keep any mention brief to stay on point.)

### Network, Version 1.1

I had gained a few new housemates by the summer of 2017, and the questionable WiFi system needed to be improved. However, I didn’t understand the problem, nor was I familiar with contemporary solutions, so I replaced the AirPort Extreme with an [AirPort Extreme 802.11ac](https://support.apple.com/kb/SP680?locale=en_US), which somewhat improved WiFi coverage. We also connected a few devices via Ethernet to mitigate some unresolved issues, bringing overall home network connectivity to "good enough."

### NAS, Version 1

With more people living in the home and less space to store things, I looked at what I could discard. I had too many hard drives, so I decided to buy a [network-attached storage (NAS)](https://en.wikipedia.org/wiki/Network-attached_storage) device to:

1. **Consolidate into a single device.** I had 4 USB 2.0 drives, 1 FireWire 400/800 drive, 2 USB 3.0 drives, and 1 Thunderbolt 2 drive. Apple went all-in on USB-C/Thunderbolt 3 in 2016, so the clock was ticking on my ability to connect some of the drive enclosures. I was particularly concerned about the FireWire enclosure, which not only had an obsolete connector but also had two disks in a [RAID 0](https://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_0) configuration _with my most precious data_, and I was not confident this would be readable by another enclosure if that were to become necessary[[2](#_footnotedef_2)].
2. **Improve hardware failure resiliency.** I’ve had two hard drives fail while in use. One did not have any backups, and that was very painful. I thought I was safe for a while as the drive was new, but it failed within three months of purchase. The other drive failure was a backup drive, which I replaced without additional trouble.
3. **Make the data accessible.** I didn’t have a desk at home, so mounting a drive required putting it somewhere stable (all the drives were spinning disks), finding the correct power adapter and data cable, and plugging everything in. While workable for occasional use, a network mount is far easier to attach and usable anywhere in the home.

At the time, I thought of network-attached storage as _just_ storage available via a network mount, so I wondered why so many NAS devices had a wide range of processor and RAM specs. Instead of taking time to resolve that confusion, I just bought the lowest spec’d device I could find with good reviews, the [Synology DS216+II](https://global.synologydownload.com/download/Document/Hardware/DataSheet/DiskStation/16-year/DS216+II/enu/Synology_DS216_PlusII_Data_Sheet_enu.pdf), and installed two [10 TB 7200 RPM Deskstar NAS hard drives](https://documents.westerndigital.com/content/dam/doc-library/en_us/assets/public/western-digital/product/hgst/deskstar-nas/data-sheet-deskstar-nas-internal-drive-kit.pdf), the largest supported capacity, in a [RAID 1](https://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_1) configuration.

The Synology gained more responsibilities over time (which it handled well despite being so woefully under-spec’d), and the hardware is still running strong.

### Network, Version 2

In the summer of 2018, we tried to set up a projector with an Apple TV on the rooftop deck, but the WiFi coverage needed improvement, and there was no Ethernet wiring nearby. Apple had officially discontinued its AirPort product line, so I decided to replace the AirPort products with a new system. I installed [eero Pros (2nd Generation)](https://www.amazon.com/dp/B07DPNSW6P/) where Ethernet was available and added an [eero Beacon](https://www.amazon.com/dp/B07DPND6BB/) next to the rooftop deck door. Finally, WiFi coverage was excellent throughout the house and rooftop deck!

### Network, Version 2.1

A few months into working from home in the summer of 2020, I was fortunate enough to have [CenturyLink Fiber Internet](https://www.centurylink.com/internet/) installed the first day it was available. A 940 Mbps symmetrical connection was a massive improvement over the 50/10 Mbps Xfinity Cable Internet and $20/month less expensive!

I had previously moved to a new house and its modem/router setup differed from the townhouse: a media cabinet housed the cable modem and an eero Pro, and the eero Pro had an Ethernet connection to the wiring enclosure with a switch to connect the other access points in the house.

The Fiber Internet connection ran into the wiring cabinet from the exterior connection point, necessitating a new router placement. I thought about getting an additional eero Pro for the wiring cabinet but didn’t want to spend that much money on a router when CenturyLink provided an [Actiontec C3000A](https://www.centurylink.com/home/help/internet/modems-and-routers/actiontec-c3000a.html) for free. And I wanted to avoid installing a WiFi access point in a metal box again, especially since it was close to access points in more ideal positions.

So, I went with the path of least resistance: I used the Actiontec C3000A as the router in the wiring cabinet and reconfigured the eero Pro in the media cabinet to be just an access point.

### Mac Hosts, Version 1

Apple announced its transition from Intel CPUs to Apple Silicon in the summer of 2020. I picked up a [Mac mini (2018)](https://support.apple.com/kb/SP782?locale=en_US) to ensure I had an Intel Mac for testing purposes that would last through the tail end of the Intel Mac install base. And I also got a [Mac mini (M1, 2020)](https://support.apple.com/kb/SP823?locale=en_US) to have an entry-level, first-generation Apple Silicon Mac for testing.

### NAS, Version 1.1

In late 2020, I added two more services to the Synology, so it was no longer _just_ network-attached storage.

We use HomeKit a lot but had a few devices that were not HomeKit compatible. After learning about [Synology’s Docker support](https://www.synology.com/en-us/dsm/feature/docker), I installed a [Homebridge](https://homebridge.io/) container and had the non-compatible devices working with HomeKit in an evening.

Before moving to Seattle, I had digitized many years of home video. Now with sufficient uplink bandwidth, and after recovering the files from the disks in the FireWire enclosure, I wanted to make the footage easily watchable by family (and at home). I experimented with [Synology Video Station](https://www.synology.com/en-global/dsm/feature/video_station), which worked, but the experience was clunky. So, I tried [Plex](https://www.plex.tv/). While it was more work to set up, it was more accessible to everyone, which is why I chose it for serving video from the Synology.

### Lab, Version 1

I had a hard time finding a good location for the Synology. It required Ethernet connectivity but also needed protection from accidental impact. The only location meeting those requirements was the media cabinet for the TV. But, this wasn’t an ideal location because the Synology created background noise, affecting the use of the room and watching TV.

After some consideration, I purchased a [wall mount rack](https://www.amazon.com/dp/B08P25PBSR/) to install in the mechanical room. I chose a wall mount to protect the electronics from flooding by keeping them away from the floor and chose a rack for additional protection from accidental impact (vs., e.g., a shelf). The mechanical room doesn’t have Ethernet, but I was able to run a line from a nearby port in the adjacent room.

I would not recommend this approach. The rack transferred the noise from the Synology into the wall into the adjacent room (though, in this case, it was less disruptive). And the rack I chose does not have sufficient depth to support some rack mount servers.

### NAS, Version 1.2

I almost omitted this section because it’s embarrassing. I did not have a regular backup of my primary computer and didn’t enable [Time Machine](https://kb.synology.com/en-us/DSM/tutorial/How_to_back_up_files_from_Mac_to_Synology_NAS_with_Time_Machine#x_anchor_id4) support on the Synology until September 2021, nearly four years after I purchased it 🤦‍♂️.

### Lab, Version 1.1

When we have high winds, heavy precipitation, or receive a lot of snow, we sometimes experience small power fluctuations or outages. In the late fall and early winter of 2021, we had many such events, and I was worried this might damage or corrupt the disks in the Synology. I purchased a [CyberPower 1500VA/900W Uninterruptible Power Supply](https://www.amazon.com/dp/B000FBK3QK/) (UPS) to ensure future fluctuations would not affect the Synology, and to ensure the Synology would have time to shut down during an outage safely.

### Network, Version 2.2

By early 2022, I was experiencing a high disruption rate in my work VPN connection. I don’t know if the Actiontec C3000A router had an increased failure rate, if my home network traffic had increased beyond the router’s capabilities, or if the problem had always existed but had become more noticeable.

As most hypotheses pointed at the router, I did not attempt to root cause the issue and replaced it with a [Ubiquiti _Edge_Router 12](https://dl.ubnt.com/datasheets/edgemax/EdgeRouter_DS.pdf). The results were fantastic—there was a notable increase in network throughput and no interrupted connections.

### NAS, Version 1.3

Many companies are exploring calendar management and sharing solutions, but address books and contacts get less attention. I have some use cases for contact sharing, so I installed [Synology Contacts](https://www.synology.com/en-global/dsm/feature/contacts) to see how well it could support my needs. It does work well in limited scenarios, and I am using it for now, but I’m also looking for a more sophisticated solution.

### NAS, Version 1.4

I use [NetNewsWire](https://netnewswire.com/) to follow many feeds and blogs. Unfortunately, I’ve been unable to get [iCloud syncing](https://netnewswire.com/help/iCloud) to work for unknown reasons. I wanted to sync feeds and read state across devices, so during the holiday break in December 2022, I set up a [FreshRSS](https://www.freshrss.org/) container on the Synology and migrated my feeds to the self-hosted service. Using NetNewsWire as my primary client and FressRSS as the backend has worked quite well.

## Summary

Over the course of 8+ years, my home computing infrastructure grew from a naïve router/WiFi access point installation to an eclectic mix of hardware supporting a half dozen services. By the end of April 2023, my home lab consisted of the following:

**Hardware:**

- [CyberPower 1500VA/900W UPS](https://www.amazon.com/dp/B000FBK3QK/)
- [ECHOGEAR 10U Network Rack](https://www.amazon.com/dp/B08P25PBSR/)
- Three [eero Pros (2nd Generation)](https://www.amazon.com/dp/B07DPNSW6P/) and one [eero Beacon](https://www.amazon.com/dp/B07DPND6BB/)
- [Synology DS216+II](https://global.synologydownload.com/download/Document/Hardware/DataSheet/DiskStation/16-year/DS216+II/enu/Synology_DS216_PlusII_Data_Sheet_enu.pdf) with two [10 TB 7200 RPM Deskstar NAS hard drives](https://documents.westerndigital.com/content/dam/doc-library/en_us/assets/public/western-digital/product/hgst/deskstar-nas/data-sheet-deskstar-nas-internal-drive-kit.pdf)
- [Mac mini (2018)](https://support.apple.com/kb/SP782?locale=en_US)
- [Mac mini (M1, 2020)](https://support.apple.com/kb/SP823?locale=en_US)
- [Ubiquiti _Edge_Router 12](https://dl.ubnt.com/datasheets/edgemax/EdgeRouter_DS.pdf)

**Services:**

- [FreshRSS](https://www.freshrss.org/)
- [Homebridge](https://homebridge.io/)
- [Plex](https://www.plex.tv/)
- [SMB File Services](https://kb.synology.com/en-sg/DSM/help/DSM/AdminCenter/file_winmacnfs_desc?version=7)
- [Synology Contacts](https://www.synology.com/en-global/dsm/feature/contacts)
- [Time Machine](https://kb.synology.com/en-us/DSM/tutorial/How_to_back_up_files_from_Mac_to_Synology_NAS_with_Time_Machine#x_anchor_id4)

During that time, as requirements changed, I decommissioned and replaced the following hardware:

- [Actiontec C3000A](https://www.centurylink.com/home/help/internet/modems-and-routers/actiontec-c3000a.html)
- [AirPort Extreme 802.11ac](https://support.apple.com/kb/SP680?locale=en_US)
- [AirPort Express 802.11n (2nd Generation)](https://support.apple.com/kb/SP651?locale=en_US)
- [AirPort Extreme 802.11n (2nd Generation)](https://support.apple.com/kb/SP671?locale=en_US)

---

[1](#_footnoteref_1). I no longer have my first AirPort Extreme device and, perhaps unsurprisingly, cannot recall its model. The only thing I know for sure was that it was the short, square box and, therefore, not the sixth generation. I’m pretty sure it had gigabit Ethernet because I was annoyed the AirPort Express did not. I maybe vaguely recall it did not support a guest network and only implemented the 802.11n draft specification, which, if correct, identifies it as the [AirPort Extreme 802.11n (2nd Generation)](https://support.apple.com/kb/SP671?locale=en_US).

[2](#_footnoteref_2). Unfortunately, my suspicions were correct. The enclosure failed before I could transfer the data, and I could not mount the stripe set using a different enclosure or software RAID. Luckily, I successfully reverse-engineered the striping scheme and reconstructed the volume manually, which I’ll post about in the future.
