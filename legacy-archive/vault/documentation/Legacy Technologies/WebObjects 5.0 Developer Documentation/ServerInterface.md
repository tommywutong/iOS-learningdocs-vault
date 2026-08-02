---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Protocols/ServerInterface.html
archived_at: '2026-07-15T08:12:46.260966Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

# ServerInterface

> **__Package:__**
> : com.webobjects.directtoweb

---

## Interface Description

---

This interface is used internally by WebObjects and should be considered private. It should not be used or implemented.

## Method Types

---

> **Private Methods**
> : [newConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6u3foj3gk4sjnz2gk4tgmfrwkl3omv3ug33onzswg5djn5xc65tpnfsc6kcbonzws43umfxhiq3pnzxgky3unfxw4ki)
> : [removeConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6u3foj3gk4sjnz2gk4tgmfrwkl3smvww65tfinxw43tfmn2gs33of53g62lef4uec43tnfzxiyloorbw63tomvrxi2lpnyuq)
> : [responseTo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6u3foj3gk4sjnz2gk4tgmfrwkl3smvzxa33oonsvi3zpifzxg2ltorqw45cqmfrwwzluf4uec43tnfzxiyloorigcy3lmv2cyqltonuxg5dbnz2eg33onzswg5djn5xcs)
> : [resynchronizeResponseTo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6u3foj3gk4sjnz2gk4tgmfrwkl3smvzxs3tdnbzg63tjpjsvezltobxw443fkrxs6qltonuxg5dbnz2fayldnnsxilziifzxg2ltorqw45cqmfrwwzlufraxg43jon2gc3tuinxw43tfmn2gs33ofe)
> : [sessionID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6u3foj3gk4sjnz2gk4tgmfrwkl3tmvzxg2lpnzeuil2torzgs3thf4ucs)

## Methods

---

### newConnection

abstract public void newConnection(AssistantConnection aConnection)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

### removeConnection

public abstract void removeConnection(AssistantConnection aConnection)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

### responseTo

public abstract AssistantPacket responseTo(AssistantPacket aPacket, AssistantConnection aConnection)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

### resynchronizeResponseTo

abstract public AssistantPacket resynchronizeResponseTo(AssistantPacket aPacket, AssistantConnection aConnection)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

### sessionID

abstract public String sessionID()

This method is intentionally undocumented. You should never have to invoke or customize it.

---

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
