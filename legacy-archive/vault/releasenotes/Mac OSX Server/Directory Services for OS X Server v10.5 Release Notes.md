---
title: Directory Services for OS X Server v10.5 Release Notes
apple_id: TP40006219
resource_type: Release Note
platform: macOS
topic: Networking, Internet, & Web
technology: DirectoryService
published: '2007-06-08'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSXServer/RN-DirectoryServices/index.html
archived_at: '2026-07-18T02:58:56.074847Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Directory Services for OS X Server v10.5 Release Notes

This document describes changes, updates, and workarounds for Directory Services for OS X Server v10.5.

#### Contents:

- [Converting Scripts for Leopard](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3demjzfvcg63tujruw422fnrsw2zlooreuixzr)
- [Checking/Manipulating the DS SearchPath from the CLI](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3demjzfvcg63tujruw422fnrsw2zlooreuixzs)
- [Removing "DisabledUser" Cached Accounts Script-o-matically](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3demjzfvcg63tujruw422fnrsw2zlooreuixzt)
- [Turning on DS Debugging](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3demjzfvcg63tujruw422fnrsw2zlooreuixzu)
- [NTLM/SMB Client Authentication to AD Checklist](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3demjzfvcg63tujruw422fnrsw2zlooreuixzv)

### Converting Scripts for Leopard

The following commands are no longer available in Leopard:

- `lookupd`
- `memberd`
- `nigrep`
- `nicl`
- `niutil`
- `niload`
- `nidump`

Here is an example of a script that will not work in Leopard because it uses using `nigrep` and `nicl` commands. The script is intended to remove cached mobile user accounts from the local node.

```

# Script to remove cached accounts in the local DS node
# Run this script as root or with sudo
# This will not run in Leopard!
#!/bin/sh


nigrep 'LocalCachedUser' / /users | while read dirid userpath authauth authtype; do            # get a list of all users with authauthority containing "LocalCachedUser"
    echo $userpath | tr -d : | while read nipath; do                                        # figure out the path to the record in the local node
        nicl / -delete $nipath                                                                # delete the cached account
    done
done
```

To do the same thing without `nigrep` and `nicl`, we substitute `dscl`:

```

# Script to remove cached accounts in the local DS node
# This should work in both Tiger and Leopard
# Run this script as root or with sudo
#!/bin/sh

# dscl searching only does exact matches.  So we list the records and pipe them through to grep to find the list of records we want.  The first column will be the username and we get that using awk.
# We also remove the line endings with tr to make it one long string.

for cuser in `dscl . -list /Users AuthenticationAuthority | grep LocalCachedUser | awk '{print $1}' | tr '\n' ' '`; do
    dscl . -delete /Users/$cuser                    # now we delete the record using dscl
done
```


### Checking/Manipulating the DS SearchPath from the CLI

To see what nodes are in your search path, you can use the command `dscl /Search -read /` and see what is listed for the `CSPSearchPath` attribute. To add nodes to the search path:

```

dscl /Search -create / SearchPolicy CSPSearchPath
dscl /Search -append / CSPSearchPath /Active\ Directory/All\ Domains
```

Don't forget to escape spaces with a backslash or use quotes around values with spaces ("/Active Directory/All Domains"). To change the order of the nodes, change the index of the node in the `CSPSearchPath`list:

```

dscl localhost changei /Search CSPSearchPath 1 /LDAPv3/moof.apple.com
dscl localhost changei /Search CSPSearchPath 2 /LDAPv3/foom.apple.com
```

Indexing starts at 0, but the node at index 0 will always be the local node. This is not editable. An index of 1 is the first non-local node in the list. In the above example, your authentication path would be:

Default Local Node (Netinfo or DSLocal)

`/LDAPv3/moof.apple.com`

`/LDAPv3/foom.apple.com`

### Removing "DisabledUser" Cached Accounts Script-o-matically

```

# This should work in both Tiger and Leopard
# Run this script as root or with sudo
#!/bin/sh
for cuser in `dscl . -list /Users AuthenticationAuthority | grep DisabledUser | awk '{print $1}' | tr '\n' ' '`; do
    dscl . -delete /Users/$cuser
done
```


### Turning on DS Debugging

```
sudo killall -USR1 DirectoryService
```

Start debugging automatically at startup:

```
touch /Library/Preferences/DirectoryService/.DSLogDebugAtStart
```

Log file:

`/Library/Logs/DirectoryService/DirectoryService.debug.log`

### NTLM/SMB Client Authentication to AD Checklist

Testing authentication of a user against a directory node:

Standard Authentication:

```
dirt -u username -p password
```

`ntlm` authentication:

```
dirt -u username -p password -a nt
```

Troubleshooting:

- Run `dsconfigad -enablesso`after binding

- Verify the following options in `/etc/smb.conf`

```

workgroup = ETS                    # this should be the netbios name of your AD domain
security = ads                    # use "ads" for this value -- "domain" will periodically change the computer trust account and break your binding to AD
netbios name = bog                # this should be the same as the computer name you used in Directory Access/Directory Utility to bind to AD
use spnego = yes                # this should always be "yes" -- it enables negotiation of the authentication methods
realm = ETS.APPLE.COM            # This should be your AD domain in all caps -- it is case sensitive!
```

- Verify that winbindd is running on the OS X Server. There should be 2 processes. If it is not, start it:
`/usr/sbin/winbindd -s /Library/Preferences/DirectoryService/winbindd.conf`

- Verify that samba and the AD plugin are using the same machine trust account password.

Step 1: Get the password that the AD plugin is using:
In the `/Library/Preferences/DirectoryService/ActiveDirectory.plist` file, look for the section that looks like:

```

<key>AD Computer Password</key>
<data>
ZW5jb2RlIG1lCg==
</data>
```

Step 2: The data field here is base64 encoded. Decode it:

```
echo "ZW5jb2RlIG1lCg==" | openssl enc -base64 -d
```

Step 3: Now compare it with the value stored by samba in `/var/db/samba/secrets.tdb`:

```
sudo tdbdump /var/db/samba/secrets.tdb
```

You should see a record that looks like:

```

{
key = "SECRETS/MACHINE_PASSWORD/ETS"
data = ",X2IgQ9sIgpByU"
}
```

If the data value here does not match the value you got from step 2, reset it:

```
sudo net -f changesecretpw
```

When prompted for a password, enter the value that was returned by step 2.
