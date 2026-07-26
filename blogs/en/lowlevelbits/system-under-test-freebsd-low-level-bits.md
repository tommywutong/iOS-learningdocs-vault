---
title: 'System Under Test: FreeBSD - Low Level Bits 🇺🇦'
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/system-under-test-freebsd/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:838b2654e4f8963b'
translated: false
---

> 原文：[System Under Test: FreeBSD - Low Level Bits 🇺🇦](https://lowlevelbits.org/system-under-test-freebsd/)　·　Low Level Bits (Alex Denisov)

# System Under Test: FreeBSD

_Published on Mar 31, 2016_

**UPD:** The series of blog-posts “System Under Test” became a full-fledged project and has moved to its own [domain](http://systemundertest.org). The most recent version of this article lives [here](http://systemundertest.org/freebsd) now.

This article is part of series [“System Under Test”](https://lowlevelbits.org/system-under-test). It provides an overview of the FreeBSD test suite and tools FreeBSD developers use to write and run tests.

### What is the project about?

FreeBSD is a well known Unix-based operating system.

### Tests

FreeBSD has one test suite. It contains ~3.6k tests and takes ~7.5 minutes to run on a virtual machine with 2Gb of RAM.

#### Getting Tests

The tests can be found in `/usr/tests` directory. Though, you may not have them there because of one of the following reasons:

1. Test suite is not a part of any distribution prior to FreeBSD 10.0.
2. Test suite is available out of the box only on FreeBSD 11.0 and newer.

If you are on FreeBSD 10.0 and want to see tests, then you just need to re-build the system from sources. Fortunately, it is very easy:

```bash
echo "WITH_TESTS=YES" >> /etc/src.conf
cd /usr/src
make buildworld
make installworld
```

#### Running tests

FreeBSD adopted approach used by NetBSD project. Within the approach they included the toolchain: [Kyua](https://github.com/jmmv/kyua) and [ATF](https://github.com/jmmv/atf/).

Initially ATF provided both tools (e.g. test runner, report generator, etc.) and libraries (e.g. test cases, assertions, etc.). Over the years tools from ATF were replaced by Kyua.

To run tests you need to point `kyua` to a `Kyuafile`.

```bash
cd /usr/tests
kyua test -k ./Kyuafile
```

when it’s done you may request report:

```bash
kyua report
```

which shows brief information for all non-succeeded test and a summary, such as this one:

![Test report](https://lowlevelbits.org/img/sut_freebsd/test_report.png)

#### Toolchain

`Kyuafile` specifies which tests to run. It also can include other `Kyuafile`s. Here is an example:

```
include('lib/Kyuafile')
atf_test_program{name=’some_atf_test'}
plain_test_program{name='some_plain_test'}
tap_test_program{name='some_tap_test’}
```

When run `kyua` will execute all tests specified in `lib/Kyuafile` (and in `Kyuafile`s included from `lib/Kyuafile`), and then will execute three tests: ATF test `some_atf_test`, plain test `some_plain_test`, and [TAP](https://en.wikipedia.org/wiki/Test_Anything_Protocol) test `some_tap_test`.

Plain test is basically a simple program that returns non-zero if test failed and zero otherwise.

TAP tests are any possible tests, the only important thing there is an output. If test prints “ok whatever” then it succeeded, if it prints “not ok whatnot” - it has failed.

ATF tests intended to be more sophisticated. They may contain several test cases per file and provide useful information besides the exit code. Also, the tests may be written using C, C++ and shell.

Here is a part of an ATF test written in shell:

```bash
username="test5678901234567"

atf_test_case longname cleanup

longname_head() {
  atf_set "require.user" "root"
  atf_set "descr" "Test that usernames longer than 16 " \
    "characters are allowed (PR bin/39546)"
}

longname_body() {
  atf_check -s exit:0 -o ignore -e ignore -x "pw useradd $username"
}

longname_cleanup() {
  atf_check -s ignore -o ignore -e ignore -x "pw userdel $username"
}

atf_init_test_cases() {
  atf_add_test_case longname
}
```

If you try to find there a test written let’s say in C, then you will not succeed. All tests under `/usr/tests` are executables. The reason is that FreeBSD tools and libraries usually have their tests source code in their source tree. During installation these tests are compiled and copied to the `/usr/tests`. For example, if you want to see tests for libc’ stdio, then you need to look at `/usr/src/lib/libc/tests/stdio`. At the moment there is one test, here is part of it:

```c
ATF_TC_WITHOUT_HEAD(test_append_binary_pos);
ATF_TC_BODY(test_append_binary_pos, tc)
{
  /*
  * For compatibility with other implementations (glibc), we set the
  * position to 0 when opening an automatically allocated binary stream
  * for appending.
  */

  FILE *fp;

  fp = fmemopen(NULL, 16, "ab+");
  ATF_REQUIRE(ftell(fp) == 0L);
  fclose(fp);

  /*
  * Make sure that a pre-allocated buffer behaves correctly.
  */
  char buf[] = "Hello";
  fp = fmemopen(buf, sizeof(buf), "ab+");
  ATF_REQUIRE(ftell(fp) == strlen(buf));
  fclose(fp);
}
```

### Conclusion

FreeBSD has ~3.6k tests. The amount of tests is suspiciously small for such a big project. Since I was (and still am) afraid that I missed some important part I did ask on mailing list [question about available tests](https://lists.freebsd.org/pipermail/freebsd-testing/2016-March/001306.html), but didn’t get any answer so far.

FreeBSD has lots of various tools and libraries, but not all of them tested.

Maybe it’s a good starting point for a contribution?

### Further reading

- man 7 tests
- [FreeBSD Test Suite](https://wiki.freebsd.org/TestSuite)
- [Kyua: An introduction for NetBSD users](https://wiki.netbsd.org/kyua/)
- [Kyua: project wiki](https://github.com/jmmv/kyua/wiki/About)
- [Test Anything Protocol](https://en.wikipedia.org/wiki/Test_Anything_Protocol)
