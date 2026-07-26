---
title: Debugging file corruption on iOS
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2014/08/12/ios/debugging-file-corruption-on-ios/'
original_language: en
published: 2014-08-12
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:deb8e696bf3d7b5f'
translated: false
---

> 原文：[Debugging file corruption on iOS](https://engineering.fb.com/2014/08/12/ios/debugging-file-corruption-on-ios/)　·　Meta Engineering — iOS

The ability to work at scale is one of the most exciting parts of engineering at Facebook. However, certain fundamental programming challenges inevitably become more difficult with scale. Debugging, for example, can prove difficult even if you can reliably reproduce the problem – and this difficulty increases when debugging a highly visible but nondeterministic issue in a rapidly changing codebase. Recently, we solved a long-term mobile debugging problem and reduced the crash rate for people using the Facebook for iOS app by more than 50 percent.

Several months ago, one of our top crashes on iOS was manifesting itself in Apple’s Core Data system, an object-relational mapper into the underlying database (SQLite). We were receiving these crashes into our crash report analyzer, but it took months to figure out the right angle to approach the problem from. Using [Hipal](https://www.facebook.com/note.php?note_id=114588058858) and [Scuba](https://www.facebook.com/publications/148418812023978/) to query and aggregate across reports, we found out that the Code Data error code numbers varied across half a dozen different manifestations.

First, we tried to identify when the problem started occurring. We currently have a monthly release cycle, but we often have hundreds of developers committing to each release. While we were able to narrow the timeframe, we couldn’t isolate further than a couple thousand commits. We didn’t have the ability to limit ourselves to just commit alterations, either. With multiple [A/B tests](https://engineering.fb.com/posts/520580318041111/airlock-facebook-s-mobile-a-b-testing-framework/) changing over each release, we couldn’t verify whether the change was related to code or configuration.

With such a wide domain of potential causes, we next focused on trying to gather hypotheses. We came up with a number of different theories about race-condition situations, architectural changes, and even false fundamental premises. For example, “Core Data is always flagged as the problem, but maybe it’s not the root cause.” With this in mind, we identified a piece of affected code where we could easily switch from Core Data to SQLite to start testing our hypothesis.

Shortly after pushing the SQLite change to our development environment, we got a corruption crash report for the new code. Our first breakthrough! We looked at the list of potential causes offered by SQLite, and the first reason mentioned was “File overwrite by rogue thread or process” [http://sqlite.org/howtocorrupt.html]. Given the rate of the problem and simplified access pattern for our code change (serialized, easy to reason, thread-safe), we had probable cause.

Next, we needed to find a “rogue thread or process” in a massive codebase. We decided to open a honeypot file right before we would otherwise open the SQLite file. If anyone were to write to this file, we would have our hypothesis’ proof and corruptor output. We would then attach the corrupted file to our crash report for analysis.

We gathered all crash report attachment data the next day. Using a hex analyzer, we found a common prefix across the attachments: 17 03 03 00 28. We then used “lldb” to set a conditional breakpoint to identify who sends “similar” content to the POSIX write() command:

```
breakpoint set -n write -c "(*(char**) ($esp + 8))[0]==0x17 
    && (*(char**) ($esp + 8))[1]==0x03 
    && (*(char**) ($esp + 8))[2]==0x03 
    && (*(char**) ($esp + 8))[3]==0x00
    && (*(char**) ($esp + 8))[4]==0x28"
```

We surfed around Facebook a little bit in the simulator and – BAM – we had multiple breakpoint stops within our SPDY network stack.

We now had circumstantial evidence, so we next wanted direct proof that the networking stack was writing to the wrong place. Upon detection, we knew we should synchronously abort the process and analyze the problematic stack trace. To accomplish this, we needed to intercept the write family of POSIX system calls (write, writev, pwrite). We decided to use [Fishhook](https://github.com/facebook/fishhook), a project that our colleagues developed and open-sourced last year to easily rebind system APIs.

```
// setup a honeypot file
int trap_fd = open(…); 
// Create new function to detect writes to the honeypot
static WRITE_FUNC_T original_write = dlsym(RTLD_DEFAULT, "write");;
ssize_t corruption_write(int fd, const void *buf, size_t size) { 
  FBFatal(fd != trap_fd, @"Writing to the honeypot file");
}
return original_write(fd, buf, size);
}
// Replace the system write with our “checked version”
rebind_symbols((struct rebinding[1]){{(char *)"write", (void *)corruption_write}}, 1);
```

We committed this code and had a new crash report pointing to the networking stack by the next day. The SSL layer was writing to a socket that was already closed and subsequently reassigned to our database file. Corpus Delicti!

Finally, we needed to analyze the problematic code for a solution. Our file descriptor retention policy looked suspect. Although SPDY used the recommended CFSocket wrapper for our database, the SSL layer did not. The SSL layer instead handled a raw file descriptor and, consequently, lifetime handling was not automatically synchronized. The SPDY socket closed before the SSL and created a race window where writes would go to a file that was “lucky enough” to receive the same file descriptor as the recently closed socket.

We worked with the networking team and fixed this issue within hours. This fix cut the Facebook iOS app crash rate in half and put a longstanding problem to rest. It turns out that abandoning manual code analysis was a good strategy. The bug surfaced with existing code that was exercised more as we ramped up default secure connections for all our users.

Dealing with a large, rapidly evolving codebase can seem overwhelming at times. Everyday tasks like analyzing crashes and understanding code can turn into their own programming challenges. At these moments, it’s important to work together, brainstorm, and rely on computer programming fundamentals. Happy hunting!

_Slobodan Predolac and Nicolas Spiegelberg, who love creating solid Facebook iOS infrastructure in the Big Apple._
