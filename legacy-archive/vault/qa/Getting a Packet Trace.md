---
title: Getting a Packet Trace
apple_id: DTS10001707
resource_type: QA
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2016-08-30'
source_url: https://developer.apple.com/library/archive/qa/qa1176/_index.html
archived_at: '2026-07-27T07:25:59.091608Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1176

# Getting a Packet Trace

## Q:  I'm trying to debug a network problem. How do I get a packet trace?

A: This depends on your platform:

- There are a number of programs for macOS that let you gather and analyze packet traces. See [macOS Programs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydcnzqg4wugsbrfvjukq2nifbvauspi5jectkt) for details.
- iOS does not support packet tracing directly. However, if you connect your iOS device to a Mac via USB, you can use an macOS packet trace program to gather and analyze traces using the remote virtual interface feature. See [iOS Packet Tracing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydcnzqg4wugsbrfvjukq2jj5jvaqkdjncvivcsifbustsh) for details.

Finally, [Packet Trace Notes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydcnzqg4wugsbrfvjukq2oj5kekuy) offers some hints and tips that you might find useful when dealing with packet traces.

__Important:__ Mention of third party sites and third party products is for informational purposes only and constitutes neither an endorsement nor a recommendation. Apple assumes no responsibility with regard to the selection, performance, or use of these vendors or products.

## macOS Programs

macOS supports a wide range of packet trace programs, as described in the following sections.

### Charles HTTP Proxy

[Charles](https://www.charlesproxy.com/) is an HTTP proxy that allows you to view all of the HTTP and HTTPS traffic between your machine and the Internet.

### CPA

[Cocoa Packet Analyzer](http://www.tastycocoabytes.com/cpa/index.php) is a native macOS implementation of a network protocol analyzer and packet sniffer.

### Debookee

[Debookee](https://www.iwaxx.com/debookee/) is a macOS application which allows you to see what your devices are sending over the network.

### HTTP Scoop

[HTTP Scoop](http://www.tuffcode.com/) is an HTTP protocol analyzer for macOS. It reconstructs complete HTTP conversations (rather than just showing the packets that make them up) and presents them in a user-friendly manner.

### IPNetMonitorX

[IPNetMonitorX](http://www.sustworks.com/site/prod_ipmx_overview.html) is a network troubleshooting toolkit for debugging Internet service problems and optimizing performance.

### mitmproxy

[mitmproxy](https://mitmproxy.org) is an interactive console program that allows traffic flows to be intercepted, inspected, modified and replayed.

### tcpdump

This command line tool is built in to all versions of macOS, and is also available on many other Unix platforms. For a quick summary of how to use `tcpdump`, see [Getting Started With tcpdump](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydcnzqg4wugsbrfvjukq2hivkfiskoi5jviqkskrcuiv2jkrefiq2qirku2ua).

### tcpflow

If you're debugging a high-level protocol, it's nice to see the various TCP connections as streams of data rather than individual packets. The `tcpflow` tool can do that for you. If you've not used `tcpflow` before, there's a quick introduction in [Getting Started With tcpflow](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydcnzqg4wugsbrfvjukq2hivkfiskoi5jviqkskrcuiv2jkrefiq2qizge6vy).

The `tcpflow` tool is not built-in to macOS, but you can get it in a variety of ways.

- Dowload and build the source code from its [home site](http://www.circlemud.org/~jelson/software/tcpflow/).
- Install it via a 'ports' project, like [MacPorts](https://www.macports.org/), [Fink](http://www.finkproject.org/) or [Homebrew](http://brew.sh).
- Dowload a pre-built binary from [here](http://www.sustworks.com/site/news_developer_resources.html).

### tcptrace

[tcptrace](http://tcptrace.org) is an open source tool for analyzing the TCP connections in a packet trace.

### Wireshark

[Wireshark](https://www.wireshark.org/) is an open source packet analyzer that has been ported to macOS.

### Wireless Diagnostics

Wireless Diagnostics is an application built in to macOS that lets you capture a Wi-Fi level packet trace. Such traces contain more information than a standard packet trace (for example, they show Wi-Fi's link-layer retransmissions).

You can find Wireless Diagnostics in the `/System/Library/CoreServices` directory; on later systems it might be in the `Applications` subdirectory within that directory. On macOS 10.7 the application was called Wi-Fi Diagnostics.

See [Wi-Fi Capture](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydcnzqg4wugsbrfvjukq2xjfdesq2bkbkfkusf) for more information about using this tool.

[Back to Top](#)

## iOS Packet Tracing

iOS does not support packet tracing directly. However, if you're developing for iOS you can take a packet trace of your app in a number of different ways:

- If the problem you're trying to debug occurs on Wi-Fi, you can put your iOS device on a test Wi-Fi network. See [Wi-Fi Capture](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydcnzqg4wugsbrfvjukq2xjfdesq2bkbkfkusf) for details.
- If your app uses HTTP, you can configure your iOS device to use a debugging HTTP proxy (such as [Charles HTTP Proxy](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydcnzqg4wugsbrfvjukq2djbavetcfkm) or [mitmproxy](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydcnzqg4wugsbrfvjukq2njfke2ucsj5mfs)).
- In iOS 5 and later you can use the [remote virtual interface](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydcnzqg4wugsbrfvjukq2skzeq) facility.

### Remote Virtual Interface

iOS 5 added a remote virtual interface (RVI) facility that lets you use macOS packet trace programs to capture traces from an iOS device. The basic strategy is:

1. Connect your iOS device to your Mac via USB.
2. Set up an RVI for that device. This creates a virtual network interface on your Mac that represents the iOS device's networking stack.
3. Run your macOS packet trace program, and point it at the RVI created in the previous step.

To set up an RVI, you should run the `rvictl` tool as shown below.

```shell
$ # First get the current list of interfaces.
$ ifconfig -l
lo0 gif0 stf0 en0 en1 p2p0 fw0 ppp0 utun0
$ # Then run the tool with the UDID of the device.
$ rvictl -s 74bd53c647548234ddcef0ee3abee616005051ed

Starting device 74bd53c647548234ddcef0ee3abee616005051ed [SUCCEEDED]

$ # Get the list of interfaces again, and you can see the new virtual
$ # network interface, rvi0, added by the previous command.
$ ifconfig -l
lo0 gif0 stf0 en0 en1 p2p0 fw0 ppp0 utun0 rvi0
```

Now that you know the name of the RVI, you can point your packet trace tool at it. For example, here's how you might run `tcpdump` to take a packet trace from the RVI and write it to the file `trace.pcap`.

```shell
$ sudo tcpdump -i rvi0 -w trace.pcap
tcpdump: WARNING: rvi0: That device doesn't support promiscuous mode
(BIOCPROMISC: Operation not supported on socket)
tcpdump: WARNING: rvi0: no IPv4 address assigned
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on rvi0, link-type RAW (Raw IP), capture size 65535 bytes
```

When you're done you can remove the RVI with the following command.

```shell
$ rvictl -x 74bd53c647548234ddcef0ee3abee616005051ed

Stopping device 74bd53c647548234ddcef0ee3abee616005051ed [SUCCEEDED]
```

__Important:__ The RVI represents the entire networking stack of the iOS device; you cannot target a specific interface on the device as you would on the Mac (using the `-i` option to `tcpdump`). However, information about the interface is recorded in the packet metadata. You can use `tcpdump` to display (via the `-k` option) and filter on (via the `-Q` option) this metadata. See the `tcpdump` [online manual](x-man-page://1/tcpdump) for details.

### Remote Virtual Interface Troubleshooting

This section explains how to resolve some common issues with RVI.

If your Mac doesn't have the `rvictl` tool, make sure you install Xcode 4.2 or later.

If the device is running iOS 7 or later, you must use the RVI support installed by Xcode 5.0 or later.

The RVI support installed by Xcode 5.0 works best on macOS 10.9 and later. Specifically, if you run `tcpdump` on 10.8.x and see the message "unknown ip 0", you will need to update to 10.9 to access those packets via RVI.

If `rvictl` fails with the message:

```
bootstrap_look_up(): 1102
```

make sure that that the `com.apple.rpmuxd` launchd job is loaded correctly. The following command should print information about the job.

```shell
$ sudo launchctl list com.apple.rpmuxd
{
    "Label" = "com.apple.rpmuxd";
    …
};
```

If it fails, it could be because the job is unloaded. You can force it to load with the following command.

```shell
$ sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.rpmuxd.plist
```

[Back to Top](#)

## Packet Trace Notes

### Getting Started With tcpdump

To get started with `tcpdump`, try the following command.

```
sudo tcpdump -i en0 -w trace.pcap
```

The elements of this command line are:

- The `sudo` command causes `tcpdump` to run with privileges, which is necessary in order to capture network traffic.
- The `-i en0` option tells `tcpdump` to capture packets on the first Ethernet interface. By default, `tcpdump` will use the first non-loopback interface it can find (usually `en0`). To specify a different interface, just change `en0` to the BSD name of that interface. For example, the AirPort interface is typically `en1`.

  To get a list of network interfaces and their user-visible names, run the [networksetup](x-man-page://8/networksetup) tool with the `-listallhardwareports` argument.
- The `-w trace.pcap` parameter tells `tcpdump` to write the packets to a file called `trace.pcap`.

__Note:__ If you're running on a system prior to macOS 10.7 you should also supply the `-B 524288` option, which increases the packet capture buffer size to 512 KiB. This is important to avoid dropped packets on high-speed networks. See [Dropped Packets](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydcnzqg4wugsbrfvjukq2ekjhvaucfiriecq2livkfg) for more information about this. This larger buffer size is the default on macOS 10.7 and later.

If you're running on a system prior to macOS 10.6 you should also supply the `-s 0` option, which tells `tcpdump` to capture the full packet rather than just the first 68 bytes. This option is the default on macOS 10.6 and later.

In response to this command, `tcpdump` will begin to capture packets and put them in the `trace.pcap` file. When you want to stop capturing, interrupt `tcpdump` by typing ^C. You can then display the contents of the packets as text using the following command.

```
tcpdump -n -e -x -vvv -r trace.pcap
```

New elements of the command line are:

- The `-n` option means that addresses are not converted to domain names, which speeds things up considerably.
- The `-e` option causes `tcpdump` to display the link-level header for each packet.
- The `-x` option causes the contents of the packet to also be displayed in hex.
- The `-vvv` option makes `tcpdump`'s output as verbose as possible.
- By specifying `-r trace.pcap` option you tell `tcpdump` to read packets from the file `trace.pcap` rather than from a network interface. Note that you don't need privileges to do this, so running `tcpdump` using `sudo` is not required.

You can also combine these steps, as shown below, but if you do this you don't get a high-fidelity record of the packets that you captured.

```
sudo tcpdump -i en0 -n -e -x -vvv
```

You can learn about `tcpdump` from its [online manual](x-man-page://1/tcpdump) and from the book [TCP/IP Illustrated, Volume 1: The Protocols](http://www.kohala.com/start/tcpipiv1.html), W. Richard Stevens, Addison-Wesley, 1994, ISBN 0-201-63346-9. That book is also an excellent introduction to TCP/IP protocols in general.

### Getting Started With tcpflow

The `tcpflow` command makes it much easier to debug high-level protocols. For example, if you're debugging an HTTP client, you can run the following command.

```
sudo tcpflow -i en0 port 80
```

`tcpflow` will create a bunch of files in the current directory, each of which contains the reassembled contents of a single TCP stream. So, if you run `tcpflow` as shown above and then fetch the URL `http://apple.com`, you can see how the HTTP redirect works.

```shell
$ sudo tcpflow -i en0 port 80
tcpflow[953]: listening on en0
^C
tcpflow[953]: terminating
$ ls -lh
total 16
-rw-r--r-- 1 root  quinn [...] 010.000.040.015.50232-017.149.160.049.00080
-rw-r--r-- 1 root  quinn [...] 017.149.160.049.00080-010.000.040.015.50232
$ # This is the request.
$ cat 010.000.040.015.50232-017.149.160.049.00080
GET / HTTP/1.1
User-Agent: curl/7.19.4 (universal-apple-darwin10.0) libcurl/7.19.4 OpenSSL/0.9.8k zlib/1.2.3
Host: apple.com
Accept: */*

$ # And this is the response.
$ cat 017.149.160.049.00080-010.000.040.015.50232
HTTP/1.1 302 Object Moved
Location: http://www.apple.com/
Content-Type: text/html
Cache-Control: private
Connection: close

<head><body> This object may be found <a HREF="http://www.apple.com/">here</a> </body>
```

### Loopback Issues

__Important:__ You should consult the documentation that comes with your program for accurate and up-to-date information about its limitations.

Some packet trace programs have problems with packets being transferred to or from the __trace machine__ (the machine running the packet trace program). To avoid these problems, separate your trace machine from the machines whose network traffic you're tracing.

As an example of this, on macOS `tcpdump` may display the TCP checksum of packets sent by the trace machine as bad. This is because of TCP checksum offloading; packets sent by the trace machine are captured before being handed to the network adapter, so they don't have the TCP checksum set correctly. This is not a fatal problem; if the bad checksums bother you, you can turn off the check by passing the `-K` option to `tcpdump`.

### Dropped Packets

If you capture all the bytes of each packet, it's very easy to overrun the kernel's packet capture buffer. The symptoms of this overrun are that your packet trace program will report that it dropped packets.

In the case of `tcpdump`, it prints a summary of how many packets were captured, filtered, and dropped when you stop the capture. For example:

```shell
$ sudo tcpdump -i en0 -w trace.pcap
tcpdump: listening on en0, link-type EN10MB (Ethernet), capture size 65535 bytes
^C
94 packets captured
177 packets received by filter
0 packets dropped by kernel
```

If the dropped count is non-zero, you need to increase the packet capture buffer size by passing the `-B` option to `tcpdump`, as discussed earlier.

### Switches And Hubs

If you use a separate trace machine, you have to make sure that the trace machine can see the packets of interest. There are two ways to do this:

- Use a hub rather than a switch — These days it is hard to find real hubs. Most 10/100 hubs are actually switches in disguise. However, it is possible to find a 10/100 hub that only switches between the different speed segments (for example, the [SMC-EZ58xxDS](http://www.smc.com) range).
- Enable [port mirroring](https://en.wikipedia.org/wiki/Port_mirroring) — On most advanced switches it is possible to configure the switch so that all traffic is mirrored to a specific port. To learn more about this, consult the documentation for your switch.

### Capture Hints From The Wireshark Wiki

The Wireshark wiki has some really useful information about how to setup your packet tracing environment.

- The [Ethernet Capture Setup Document](https://wiki.wireshark.org/CaptureSetup/Ethernet) contains good background information for setting up your network for monitoring.
- The [Hub Reference Document](https://wiki.wireshark.org/HubReference) contains information on various types of hubs.
- The [Switch Reference Document](https://wiki.wireshark.org/SwitchReference) contains information on analysis features, such as port mirroring, found on various models of switches, including links to online documentation for those switches.

### Wi-Fi Capture

Capturing packets on Wi-Fi can be tricky because conversations between one Wi-Fi client and the access point are not necessarily visible to other Wi-Fi clients. There are two easy ways to ensure that you see the relevant Wi-Fi traffic:

- bridge mode — If your Wi-Fi access point supports bridge mode (for example, all Apple base stations do), you can bridge the Wi-Fi on to an Ethernet and then use standard Ethernet techniques to capture a packet trace. You may not be able to see Wi-Fi to Wi-Fi traffic, but in many situations that's not a problem.
- Internet Sharing — If you enable Internet Sharing on your Mac, and have your Wi-Fi clients join the shared network, you can run your packet trace program on the Mac and see all the Wi-Fi traffic. If you target the Mac's Wi-Fi interface, you will see all traffic including Wi-Fi to Wi-Fi traffic. If you target the Ethernet interface, you will only see traffic entering or leaving the Wi-Fi network.

Alternatively, you can use the [Wireless Diagnostics](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydcnzqg4wugsbrfvjukq2xjfjektcfknjuiskbi5he6u2ujfbvg) application to take a Wi-Fi level packet trace. This shows all traffic visible to your Mac, including low-level Wi-Fi traffic that's not visible with other tools. When using this tool, keep in mind the following:

- After running the application, you can access the packet trace feature by choosing Utilities from the Window menu and then selecting the Frame Capture tab.
- Your Mac can't use the Wi-Fi interface for normal network traffic while tracing.
- You must choose a channel to trace on. It simplifies things if you configure your access point to use a specific channel rather than let it choose one automatically.
- If the Wi-Fi network has a password, Wi-Fi encryption will make it much harder to examine the trace. To get around this, either temporarily turn off the Wi-Fi password on your network or use a separate test network that has no password.

### Submitting A Trace With A Bug Report

If you're submitting a bug report related to networking, you should consider submitting a packet trace along with your bug report. The [Bug Reporting](https://developer.apple.com/bug-reporting/) page has details on how to provide additional information with your bug report.

### Submitting A Trace To DTS

If you send a packet trace to DTS, please include the following:

- The system type and OS version of the trace machine.
- The name and version of the program you used to capture the packet trace.
- If you've used a program whose native file format is the [libpcap file format](https://en.wikipedia.org/wiki/Pcap) (these include `tcpdump`, Wireshark, and various others), you can send us the packet trace file in that format. Otherwise, please include a copy of the packet trace in both its native format and, if that native format isn't text, a text export of the trace as well. That way we're guaranteed to be able to read your packet trace.
- For each relevant machine shown in the trace, please describe the following:

  - the machine's role in the network conversation
  - the system type and OS version
  - the machine's IP address
  - the machine's hardware address (also known as the Ethernet address or MAC address)
[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-08-30 | Added a discussion of packet metadata in RVI packet traces. |
| 2016-08-05 | Added reference to mitmproxy. Removed reference to FrameSeer (its site is offline). Other editorial changes. |
| 2014-08-28 | Changed the RVI example to save the packet trace to disk, which is generally the most useful option (r. 15449523). |
| 2013-10-29 | Added a reference to the Wireless Diagnostics application (r. 14454725). Added the "Submitting A Trace With A Bug Report" section. Added a section on RVI troubleshooting. |
| 2013-01-31 | Added references to tcptrace (r. 11809312) and Debookee (r. 12929510). Simplified the example tcpdump command by removing options that are applied by default on recent systems. Made minor editorial changes. |
| 2012-01-05 | Documented iOS 5's remote virtual interface feature (r. 10194867), and reworked the document structure to account for that change. Added a section on Wi-Fi packet tracing. |
| 2011-03-08 | Added reference to the Charles HTTP proxy (r. 9053410). |
| 2009-10-14 | Added sections on tcpflow and HTTP Scoop. Added information about dropped packets and how to avoid them. Various minor editorial changes. |
| 2008-06-03 | Streamlined product descriptions and reorganized the Miscellaneous notes. Restructured entire document and added additional packages. Added additional Hub/Switch information. |
| 2004-07-13 | Added a reference to FrameSeer. Converted text to TNT and fixed formatting and link problems. |
| 2002-08-08 | New document that lists tools available for looking at the network packets on the wire, plus some helpful hints on how to use those tools. |
