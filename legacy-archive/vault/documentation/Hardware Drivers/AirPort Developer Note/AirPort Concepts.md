---
title: AirPort Developer Note
apple_id: TP40003030
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-04-28'
source_url: https://developer.apple.com/library/archive/documentation/HardwareDrivers/Conceptual/HWTech_Airport/Articles/AirP_concepts.html
archived_at: '2026-07-15T07:40:58.623224Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AirPort Developer Note](Introduction%20to%20AirPort%20Developer%20Note.md)


[Next](AirPort%20Product-Specific%20Details.md)[Previous](Introduction%20to%20AirPort%20Developer%20Note.md)

# AirPort Concepts

This article provides an overview of IEEE 802.11 wireless networking technology and standards and describes certain features implemented as AirPort wireless networking technology in Apple's CPU products.

The IEEE 802.11 standards provide specifications for wireless local area networks (WLANs), often called "wireless Ethernet" or Wi-Fi, that use radio instead of cables or wires for transmission of data. Wi-Fi certification, as governed by the Wi-Fi Alliance, ensures that certified WLAN products are compatible with each other. The freedom from cable infrastructure requirements and the availability of compatible but competitive components helped ensure rapid adoption of this technology.

The original 802.11-1997 standard assumed data transmission rates of up to 2 Mbps. Since then, several versions of the standard have come into practical use:

- 802.11a, at up to 54 Mbps at frequencies in the 5 GHz range
- 802.11b, at up to 11 Mbps at frequencies in the 2.4 GHz range
- 802.11g, at up to 54 Mbps at frequencies in the 2.4 GHz range
- 802.11n draft standard, at up to five times the performance and up to twice the range compared to the earlier Apple 802.11g standard implementation

802.11a provides for transmission rates up to 54 Mbps, and the 5 GHz range offers more bandwidth and less congestion than the 2.4 GHz range. One serious drawback of the 5 GHz range is that its use is restricted in several countries, often to military purposes. Signal propagation at higher frequencies can also be problematic; signals do not travel as far, they drop off rapidly, and they are less able to penetrate walls. Although the restricted market made devices more expensive, the transmission speed made 802.11a attractive to enterprise markets.

802.11b uses the popular 2.4 GHz frequency band. Frequencies within this band (with minor variations in certain countries) are available for wireless networking worldwide. With a worldwide market, conformant devices soon became affordable, spurring rapid adoption of 802.11b. One drawback, however, is that other devices such as cordless phones and microwaves can cause interference and congestion in this band.

802.11g is rapidly growing in popularity. It is backward-compatible with 802.11b, uses the same 2.4 GHz range, but provides for transmission rates up to 54 Mbps.

802.11n is based on the current draft standard specification. It adds technology called multiple-input multiple-output (MIMO), a signal processing and smart antenna technique for transmitting multiple data streams through multiple antennas. For additional information, refer to [Apple's 802.11 site](http://www.apple.com/wireless/80211/).

The nature of wireless networks presents numerous challenges not common to wired networks. Computers using the WLAN may be _portable_ (typically used at one physical location while within the coverage area of a network access point) or even _mobile_ (moving in and out of the coverage area or even between coverage areas of different network access points. The size and boundaries of the WLAN can be indeterminate and mutable due to environmental factors. Foreign radio signals can interfere with reception. And non-authorized devices can receive network traffic without a physical connection.

The 802.11 standard is designed to fit within the IEEE’s 802 family of LAN standards, particularly to allow efficient integration of WLANs and wired LANs. To this end, it defines the services that Wi-Fi equipment must provide to implement the physical and data link layers of the Open Systems Interconnect (OSI) network model so that they accommodate the special requirements of wireless networking. A network device that implements both the medium access control (MAC) and the physical interface (PHY) layers in conformance with 802.11 is known as a _station_. A station that connects other stations via _distribution services_ is known as an _access point_. A device that provides a WLAN interface to a non-802.11 LAN is known as a _portal_; it is said to _integrate_ the WLAN and the wired LAN. A single device can serve as both an access point and a portal.

In 1999, Apple was the first computer manufacturer to make 802.11b technology widely available to consumers with its AirPort wireless solution, consisting of the AirPort Card and AirPort Base Station, together providing a maximum data rate of 11 Mbps at a range of up to 150 feet. The AirPort Base Station served as a WLAN access point and as a portal to connect to 10Base-T Ethernet or to a dial-up line at 56 Kbps.

Starting in Spring 2007, most of Apple's Airport Extreme products implement the 802.11n draft standard. The 802.11n technology provides multiple-input multiple-output (MIMO), a signal processing and smart antenna technique for transmitting multiple data streams through multiple antennas. This technology is compatible with 802.11a/b/g and provides up to five times the performance and up to twice the range compared to the earlier 802.11g standard.

Software to enable 802.11n functionality is included with the AirPort Extreme Base Station (802.11n). For information on Mac computers that support 802.11n in the new AirPort Extreme Base Station using the enabler software, refer to [Apple's 802.11 site](http://www.apple.com/wireless/80211/).

The 802.11g standard offers a maximum data rate of 54 Mbps—nearly five times faster than 11 Mbps 802.11b products, such as the original AirPort products. Wi-Fi Certified 802.11g devices such as the earlier AirPort Extreme Base Station are also compatible with 802.11b; that is, 802.11g access points support Wi-Fi Certified 802.11b devices, such as the previous version of AirPort. When 802.11b devices use an AirPort Extreme Base Station, they receive the same bandwidth as they would with an AirPort Base Station or other 802.11b access point—a maximum data rate of 11 Mbps. Similarly, the 802.11g AirPort Extreme Card enables users to use both 802.11g and 802.11b networks.

A mentioned above, because 802.11g networks operate in the popular 2.4 GHz frequency band, they are occasionally subject to interference by devices such as microwave ovens, baby monitors, and cordless phones. However, such interference generally only causes a decreased data rate, not a loss of connection or loss of data. That disadvantage is offset in normal use by the more robust signals associated with the 2.4 GHz band, which readily pass through solid objects such as walls. Since AirPort Extreme operates in the 2.4 GHz frequency band, it is approved for use in the same countries as 802.11b products.

AirPort Extreme has several features designed to maintain the security of the user's data: 

- In 802.11b mode, the system uses direct-sequence spread-spectrum (DSSS) technology that uses a multibit spreading code that effectively scrambles the data for any receiver that lacks the corresponding code.
- The system can use an Access Control List of authentic network client ID values (wireless and MAC addresses) to verify each client’s identity before granting access to the network.
- When communicating with a base station, AirPort Extreme uses 64-bit and 128-bit Wired Equivalent Privacy (WEP) encryption and Wi-Fi Protected Access (WPA) personal and enterprise modes to encode data while it is in transit. Additional security features may be available via software or firmware upgrades as 802.11 enhancements are ratified by IEEE.
- The AirPort Extreme Base Station can be configured to use NAT (Network Address Translation), protecting data from Internet hackers.
- The AirPort Extreme Base Station can authenticate users by their unique Ethernet IDs, preventing unauthorized computers from logging into your network. Network administrators can take advantage of RADIUS compatibility, used for authenticating users over a remote server. Smaller networks can offer the same security using a local look-up table located within the base station. 

As an additional data security measure, Virtual Private Network (VPN) can be used in conjunction with the AirPort Extreme data security.

AirPort Extreme provides a media access controller (MAC), a digital signal processor (DSP), and a radio-frequency (RF) section in a fully-integrated, wireless LAN module compliant with the IEEE 802.11g standard using both OFDM (orthogonal frequency-division multiplexing) and DSSS technologies. Using DSSS, AirPort Extreme is interoperable with PC-compatible wireless LANs that conform to the 802.11b standard at speeds of 11 Mbps, 5.5 Mbps, 2 Mbps, and 1 Mbps. Using OFDM, AirPort Extreme is compatible with all 802.11g standard speeds. Current implementation of AirPort Extreme is based on an IEEE 802.11n draft specification and is compatible with IEEE 802.11a, IEEE 802.11b, and IEEE 802.11g.

The following software is provided to set up and use AirPort Extreme:

- AirPort Setup Assistant, an easy-to-use program that guides users through the steps necessary to set up AirPort Extreme or set up an AirPort Extreme Base Station.
- AirPort status menu, which users can use to switch between wireless networks and to create and join peer-to-peer networks.
- AirPort Admin Utility, a utility for advanced users and system administrators. With it the user can edit the administrative and advanced settings needed for some advanced configurations.
- AirPort Extreme enabler software, enables 802.11n draft standard in supported products.

[Next](AirPort%20Product-Specific%20Details.md)[Previous](Introduction%20to%20AirPort%20Developer%20Note.md)

