---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/snmp_api/CompositePage.html
archived_at: '2026-07-15T07:23:27.906396Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| snmp_api.h | snmp_api.h | snmp_api.h | snmp_api.h | snmp_api.h |

## Introduction

---

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| netsnmp_pdu | netsnmp_pdu | netsnmp_pdu | netsnmp_pdu | netsnmp_pdu |

---

__See Also:__
> **[struct snmp_pdu to netsnmp_pdu](#apple-f4xwc4dqnrsv64tfmyxwi33df52gs5dmmu5hizdfmyxxg5dsovrxi43onvyf64deov2g63tforzw43lql5ygi5i)**
> :

```
/** @struct snmp_pdu
The snmp protocol data unit.
    */
typedef struct snmp_pdu {
    /*
 * Protocol-version independent fields
        */
    /** snmp version */
    long version;
    /** Type of this PDU */
    int command;
    /** Request id - note: not incremented on retries */
    long reqid;
    /** Message id for V3 messages note: incremented for each retry
        */
    long msgid;
    /** Unique ID for incoming transactions */
    long transid;
    /** Session id for AgentX messages */
    long sessid;
    /** Error status (non_repeaters in GetBulk) */
    long errstat;
    /** Error index (max_repetitions in GetBulk) */
    long errindex;
    /** Uptime */
    u_long time;
    u_long flags;
    int securityModel;
    /** noAuthNoPriv, authNoPriv, authPriv */
    int securityLevel;
    int msgParseModel;
    /**
Transport-specific opaque data. This replaces the IP-centric address
field.
        */
    void *transport_data;
    int transport_data_length;
    /**
The actual transport domain. This SHOULD NOT BE FREE()D.
        */
    const oid *tDomain;
    size_t tDomainLen;
    netsnmp_variable_list *variables;
    /*
 * SNMPv1 & SNMPv2c fields
        */
    /** community for outgoing requests. */
    u_char *community;
    /** length of community name. */
    size_t community_len;
    /*
 * Trap information
        */
    /** System OID */
    oid *enterprise;
    size_t enterprise_length;
    /** trap type */
    long trap_type;
    /** specific type */
    long specific_type;
    /** This is ONLY used for v1 TRAPs */
    unsigned char agent_addr[4];
    /*
 * SNMPv3 fields
        */
    /** context snmpEngineID */
    u_char *contextEngineID;
    /** Length of contextEngineID */
    size_t contextEngineIDLen;
    /** authoritative contextName */
    char *contextName;
    /** Length of contextName */
    size_t contextNameLen;
    /** authoritative snmpEngineID for security */
    u_char *securityEngineID;
    /** Length of securityEngineID */
    size_t securityEngineIDLen;
    /** on behalf of this principal */
    char *securityName;
    /** Length of securityName. */
    size_t securityNameLen;
    /*
 * AgentX fields
 * (also uses SNMPv1 community field)
        */
    int priority;
    int range_subid;
    void *securityStateRef;
} netsnmp_pdu;
```

##### Discussion

\* Typedefs the snmp_pdu struct into netsnmp_pdu

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| netsnmp_session | netsnmp_session | netsnmp_session | netsnmp_session | netsnmp_session |

---

__See Also:__
> **[struct snmp_session netsnmp_session](#apple-f4xwc4dqnrsv64tfmyxwi33df52gs5dmmu5hizdfmyxxg5dsovrxi43onvyf643fonzws33onzsxi43onvyf643fonzws33o)**
> :

```
typedef struct snmp_session netsnmp_session;
```

##### Discussion

\* Typedefs the snmp_session struct intonetsnmp_session

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| netsnmp_variable_list | netsnmp_variable_list | netsnmp_variable_list | netsnmp_variable_list | netsnmp_variable_list |

---

__See Also:__
> **[variable_list](#apple-f4xwc4dqnrsv64tfmyxwgl3umfts65tbojuwcytmmvpwy2ltoq)**
> :
>
> **[struct variable_list netsnmp_variable_list](#apple-f4xwc4dqnrsv64tfmyxwi33df52gs5dmmu5hizdfmyxxg5dsovrxi5tbojuwcytmmvpwy2ltorxgk5dtnzwxax3wmfzgsylcnrsv63djon2a)**
> :

```
typedef struct variable_list netsnmp_variable_list;
```

##### Discussion

\* Typedefs the variable_list struct into netsnmp_variable_list

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| struct snmp_pdu to netsnmp_pdu | struct snmp_pdu to netsnmp_pdu | struct snmp_pdu to netsnmp_pdu | struct snmp_pdu to netsnmp_pdu | struct snmp_pdu to netsnmp_pdu |

---

__See Also:__
> **[netsnmp_pdu](#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml3omv2hg3tnobpxazdv)**
> :

```
/** @struct snmp_pdu
The snmp protocol data unit.
    */
typedef struct snmp_pdu {
    /*
 * Protocol-version independent fields
        */
    /** snmp version */
    long version;
    /** Type of this PDU */
    int command;
    /** Request id - note: not incremented on retries */
    long reqid;
    /** Message id for V3 messages note: incremented for each retry
        */
    long msgid;
    /** Unique ID for incoming transactions */
    long transid;
    /** Session id for AgentX messages */
    long sessid;
    /** Error status (non_repeaters in GetBulk) */
    long errstat;
    /** Error index (max_repetitions in GetBulk) */
    long errindex;
    /** Uptime */
    u_long time;
    u_long flags;
    int securityModel;
    /** noAuthNoPriv, authNoPriv, authPriv */
    int securityLevel;
    int msgParseModel;
    /**
Transport-specific opaque data. This replaces the IP-centric address
field.
        */
    void *transport_data;
    int transport_data_length;
    /**
The actual transport domain. This SHOULD NOT BE FREE()D.
        */
    const oid *tDomain;
    size_t tDomainLen;
    netsnmp_variable_list *variables;
    /*
 * SNMPv1 & SNMPv2c fields
        */
    /** community for outgoing requests. */
    u_char *community;
    /** length of community name. */
    size_t community_len;
    /*
 * Trap information
        */
    /** System OID */
    oid *enterprise;
    size_t enterprise_length;
    /** trap type */
    long trap_type;
    /** specific type */
    long specific_type;
    /** This is ONLY used for v1 TRAPs */
    unsigned char agent_addr[4];
    /*
 * SNMPv3 fields
        */
    /** context snmpEngineID */
    u_char *contextEngineID;
    /** Length of contextEngineID */
    size_t contextEngineIDLen;
    /** authoritative contextName */
    char *contextName;
    /** Length of contextName */
    size_t contextNameLen;
    /** authoritative snmpEngineID for security */
    u_char *securityEngineID;
    /** Length of securityEngineID */
    size_t securityEngineIDLen;
    /** on behalf of this principal */
    char *securityName;
    /** Length of securityName. */
    size_t securityNameLen;
    /*
 * AgentX fields
 * (also uses SNMPv1 community field)
        */
    int priority;
    int range_subid;
    void *securityStateRef;
} netsnmp_pdu;
```

##### Discussion

\* Typedefs the snmp_pdu struct into netsnmp_pdu

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| struct snmp_session netsnmp_session | struct snmp_session netsnmp_session | struct snmp_session netsnmp_session | struct snmp_session netsnmp_session | struct snmp_session netsnmp_session |

---

__See Also:__
> **[netsnmp_session](#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml3omv2hg3tnobpxgzltonuw63q)**
> :

```
typedef struct snmp_session netsnmp_session;
```

##### Discussion

\* Typedefs the snmp_session struct intonetsnmp_session

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| struct variable_list netsnmp_variable_list | struct variable_list netsnmp_variable_list | struct variable_list netsnmp_variable_list | struct variable_list netsnmp_variable_list | struct variable_list netsnmp_variable_list |

---

__See Also:__
> **[variable_list](#apple-f4xwc4dqnrsv64tfmyxwgl3umfts65tbojuwcytmmvpwy2ltoq)**
> :
>
> **[netsnmp_variable_list](#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml3omv2hg3tnobpxmylsnfqwe3dfl5wgs43u)**
> :

```
typedef struct variable_list netsnmp_variable_list;
```

##### Discussion

\* Typedefs the variable_list struct into netsnmp_variable_list

## Structs and Unions

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| snmp_session | snmp_session | snmp_session | snmp_session | snmp_session |

---

```
struct snmp_session {
    /*
 * Protocol-version independent fields
        */
    /** snmp version */
    long version;
    /** Number of retries before timeout. */
    int retries;
    /** Number of uS until first timeout, then exponential backoff
        */
    long timeout;
    u_long flags;
    struct snmp_session *subsession;
    struct snmp_session *next;
    /** Domain name or dotted IP address of default peer */
    char *peername;
    /** UDP port number of peer. */
    u_short remote_port;
    /** My Domain name or dotted IP address, 0 for default */
    char *localname;
    /** My UDP port number, 0 for default, picked randomly */
    u_short local_port;
    /**
Authentication function or NULL if null authentication is used
        */
    u_char *(*authenticator) (
        u_char *,
        size_t *,
        u_char *,
        size_t);
    /** Function to interpret incoming data */
    netsnmp_callback callback;
    /**
Pointer to data that the callback function may consider important
        */
    void *callback_magic;
    /** copy of system errno */
    int s_errno;
    /** copy of library errno */
    int s_snmp_errno;
    /** Session id - AgentX only */
    long sessid;
    /*
 * SNMPv1 & SNMPv2c fields
        */
    /** community for outgoing requests. */
    u_char *community;
    /** Length of community name. */
    size_t community_len;
    /** Largest message to try to receive. */
    size_t rcvMsgMaxSize;
    /** Largest message to try to send. */
    size_t sndMsgMaxSize;
    /*
 * SNMPv3 fields
        */
    /** are we the authoritative engine? */
    u_char isAuthoritative;
    /** authoritative snmpEngineID */
    u_char *contextEngineID;
    /** Length of contextEngineID */
    size_t contextEngineIDLen;
    /** initial engineBoots for remote engine */
    u_int engineBoots;
    /** initial engineTime for remote engine */
    u_int engineTime;
    /** authoritative contextName */
    char *contextName;
    /** Length of contextName */
    size_t contextNameLen;
    /** authoritative snmpEngineID */
    u_char *securityEngineID;
    /** Length of contextEngineID */
    size_t securityEngineIDLen;
    /** on behalf of this principal */
    char *securityName;
    /** Length of securityName. */
    size_t securityNameLen;
    /** auth protocol oid */
    oid *securityAuthProto;
    /** Length of auth protocol oid */
    size_t securityAuthProtoLen;
    /** Ku for auth protocol XXX */
    u_char securityAuthKey[USM_AUTH_KU_LEN];
    /** Length of Ku for auth protocol */
    size_t securityAuthKeyLen;
    /** Kul for auth protocol */
    u_char *securityAuthLocalKey;
    /** Length of Kul for auth protocol XXX */
    size_t securityAuthLocalKeyLen;
    /** priv protocol oid */
    oid *securityPrivProto;
    /** Length of priv protocol oid */
    size_t securityPrivProtoLen;
    /** Ku for privacy protocol XXX */
    u_char securityPrivKey[USM_PRIV_KU_LEN];
    /** Length of Ku for priv protocol */
    size_t securityPrivKeyLen;
    /** Kul for priv protocol */
    u_char *securityPrivLocalKey;
    /** Length of Kul for priv protocol XXX */
    size_t securityPrivLocalKeyLen;
    /** snmp security model, v1, v2c, usm */
    int securityModel;
    /** noAuthNoPriv, authNoPriv, authPriv */
    int securityLevel;
    /**
security module specific
        */
    void *securityInfo;
    /**
use as you want data
        */
    void *myvoid;
};
```

##### Discussion

The snmp session structure.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| variable_list | variable_list | variable_list | variable_list | variable_list |

---

__See Also:__
> **[struct variable_list netsnmp_variable_list](#apple-f4xwc4dqnrsv64tfmyxwi33df52gs5dmmu5hizdfmyxxg5dsovrxi5tbojuwcytmmvpwy2ltorxgk5dtnzwxax3wmfzgsylcnrsv63djon2a)**
> :
>
> **[netsnmp_variable_list](#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml3omv2hg3tnobpxmylsnfqwe3dfl5wgs43u)**
> :

```
struct variable_list;
```

##### Discussion

\* Typedefs the variable_list struct into netsnmp_variable_list

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| variable_list | variable_list | variable_list | variable_list | variable_list |

---

```
struct variable_list {
    /** NULL for last variable */
    struct variable_list *next_variable;
    /** Object identifier of variable */
    oid *name;
    /** number of subid's in name */
    size_t name_length;
    /** ASN type of variable */
    u_char type;
    /** value of variable */
    netsnmp_vardata val;
    /** the length of the value to be copied into buf */
    size_t val_len;
    /** 90 percentile < 24. */
    oid name_loc[MAX_OID_LEN];
    /** 90 percentile < 40. */
    u_char buf[40];
    /** (Opaque) hook for additional data */
    void *data;
    /** callback to free above */
    void (*dataFreeHook)(
        void *);
    int index;
};
```

##### Discussion

The netsnmp variable list binding structure, it's typedef'd to
netsnmp_variable_list.

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Last Updated: 2006-06-20
