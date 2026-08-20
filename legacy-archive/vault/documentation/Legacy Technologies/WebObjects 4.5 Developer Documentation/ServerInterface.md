---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Protocols/ServerInterface.html
archived_at: '2026-07-15T08:11:31.362650Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Direct to Web

[[Table of Contents]](../DirectToWebTOC.md)

# ServerInterface

> **__Package:__**
> : com.apple.yellow.directtoweb

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

[[Table of Contents]](../DirectToWebTOC.md)
