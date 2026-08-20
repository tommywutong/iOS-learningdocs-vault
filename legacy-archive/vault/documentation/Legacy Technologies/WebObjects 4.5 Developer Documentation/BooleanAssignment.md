---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Classes/BooleanAssignment.html
archived_at: '2026-07-15T08:11:28.453217Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Direct to Web

__BooleanAssignment__

__Package__:
com.apple.yellow.directtoweb

__Inherits from__:[Assignment](Assignment.md)

---

__Class Description__

---

This class maintains information about boolean assignments on the right hand side of rules. It should not be used, subclassed, or replaced.

__Method Types__

---

Constructors

- [public BooleanAssignment(EOKeyValueUnarchiver unarchiver)](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6qtpn5wgkyloifzxg2lhnzwwk3tuf5bg633mmvqw4qltonuwo3tnmvxhil2cn5xwyzlbnzaxg43jm5xg2zlooqxsqrkpjnsxsvtbnr2wkvlomfzgg2djozsxeki)
- [BooleanAssignment(String key, Object value)](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6qtpn5wgkyloifzxg2lhnzwwk3tuf5bg633mmvqw4qltonuwo3tnmvxhil2cn5xwyzlbnzaxg43jm5xg2zlooqxsqu3uojuw4zzmj5rguzldoquq)

---

---

__Constructors__

---

__com.apple.yellow.directtoweb.BooleanAssignment__

public BooleanAssignment(EOKeyValueUnarchiver unarchiver)

Creates and returns a BooleanAssignment object based on a EOKeyValueUnarchiver. You use this constructor to read the assignment information from a rule file.

---

__com.apple.yellow.directtoweb.BooleanAssignment__

BooleanAssignment(String key, Object value)

Creates a BooleanAssignment object, sets its key and value, and returns it.

---
