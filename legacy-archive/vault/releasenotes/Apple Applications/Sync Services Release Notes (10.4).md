---
title: Sync Services  Release Notes (10.4)
apple_id: TP40001360
resource_type: Release Note
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-07-06'
source_url: https://developer.apple.com/library/archive/releasenotes/AppleApplications/RN-SyncServices/index.html
archived_at: '2026-07-18T02:50:20.788331Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Sync Services Framework Release Notes for Mac OS X v10.4

> [!IMPORTANT]
> 

Sync Services is a framework containing all the components you need to sync your applications and devices. If your application uses Sync Services, user data can be synced with other applications and devices on the same computer, or other computers over the network via .Mac. Ideally, all Mac OS X applications should sync user data quickly and quietly in the background. Consequently, user data is available when and where the user wants it.

#### Contents:

- [General Notes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnrqfvcg63tujruw422fnrsw2zlooreuixzr)
- [ISyncManager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnrqfvcg63tujruw422fnrsw2zlooreuixzs)
- [ISyncSession](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnrqfvcg63tujruw422fnrsw2zlooreuixzt)
- [Schema Registration](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnrqfvcg63tujruw422fnrsw2zlooreuixzu)
- [Client Registration](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnrqfvcg63tujruw422fnrsw2zlooreuixzv)

### General Notes

- It's possible to end up with two SyncServers running for the same user if you ssh to a computer and run a tool that uses the Sync Services framework. This situation should be avoided.
- Sync Services doesn't respond very gracefully if its data directory goes missing (`~/Library/Application Support/SyncServices/Local`). If you manually remove the data directory, make sure you first quit all applications that are using Sync Services. Here's a quick check list:

  - quit all running applications that use Sync Services. Don't forget System Preferences
  - `/usr/bin/killall SyncServer syncuid`
  - `/usr/bin/killall SystemUIServer` if you have the Sync menuling enabled
- Safari bookmarks are not synced until Safari has been launched for the first time on a new install.
- Snapshots claim to be immutable copies of the Truth, but they are not, in fact. If you have a snapshot of the Truth, the snapshot will mutate as the Truth is updated by the SyncServer. We intend to fix this in a future release.
- There is no conflict resolution for delete/modify conflicts - deletes always win.
- When a client pushes a change that conflicts with a value in the Truth, the Truth value is propagated back to the client during the next pull phase. If multiple clients are syncing in the same session, the first client to have its changes applied to the Truth "wins" and the other clients are all given its values. This is necessary to maintain relationship integrity. When the conflict is resolved, the winning value will propagate to all clients, of course.
- Sync Services treats a false value for boolean attributes as distinct and different from the absence of such attributes. This causes bounces between clients that differ in their understand of what "NO" means. We may change this in the future to treat the absence of a boolean attribute as equivalent to a false value. Regardless, clients must respect both "false" and "null" values passed to them, and not bounce new values back to the truth.
- You should avoid relationship graphs that are cyclical. (eg. record A has a relationship to B who has a relationship back to A.) Conflict resolver can blow up if there is ever a conflict on such a relationship.
- Another reason to avoid cyclic relationship graphs: Sync Services can't match records with cyclic references in their identity keys. This causes the whole graph to be duplicated. In the special case where a record refers to itself in its identity key, the SyncServer dies with a rather nasty message.
- When matching a new record from a client to two records in the Truth with the same identity properties, Sync Services uses the non-identity attributes to try to decide the best match for the new record. It does not use the relationships in this same fashion, however, and may end up mismatching the new record if two records are identical save for their relationships.
- Sync Services does not remove a conflict if the participants in the conflict come back in to agreement on the disputed value.

### ISyncManager

- ISyncRecordSnapshot should not be used for general database-like access. The record store is optimized for SyncService's use and provides extremely poor performance for general queries. In particular, -recordsWithMatchingAttributes: should be used sparingly.
- `-ISyncManager snapshotOfRecordsInTruthWithEntityNames:` creates a new snapshot each time it is called. This is an expensive operation and the caller should cache the snapshot as appropriate.
- Sync alert tools are invoked with four arguments on the command line: "--sync" followed by the client identifier and "--entitynames" followed by a comma-separated list of the entity names the tool is being asked to sync. We may change the order of the arguments or add new arguments to the tool. You should parse for the --sync and --entitynames options explicitly rather than rely on the current order of the parameters.
- If your client syncs multiple entities, you should try to sync them all in a single session if possible. Not only is this a performance win, but you may not synchronize completely with .Mac if you do otherwise. This is because the .Mac clients syncs all entities in a single session.
- A client's sync alert tool may not be passed all supported entities on its command line when alerted to sync with some other client. For example, if client A starts syncing entities R and P, client B, who syncs entities R, P and Q, may only be passed "--entitynames R,P" on its command line. It is free to specify whatever entities it wants when creating its sync session, of course.
- Clients may be left with an invalid ISyncClient object if a client is unregistered in a different process. Subsequent calls to `-ISyncManager clientWithIdentifier:` may continue returning this invalid client for some time after the registration. The only work around is to coordinate with the unregistering process and to manually (redundantly) unregister the client in your own process.

### ISyncSession

- You should avoid providing multiple changes for the same property in an ISyncChange object. ISyncSession currently accepts these changes quietly but soon will start to complain about them.
- It is not possible to swap two record identifiers in a single call to `-ISyncSession clientChangedRecordIdentifiers:`. That is, you cannot provide a dictionary mapping A -> B and B -> A. Work-around is to perform the change in two calls to -clientChangedRecordIdentifiers:.
- The format of the callback from `-ISyncSession prepareToPullChangesInBackgroundForEntityNames:target:selector:` is not documented. It is the same as the callback from `+ISyncSession beginSessionInBackgrounWithClient:entityNames:target:selector:`:

  `- (void)client:(ISyncClient *)can beginSession:(ISyncSession *)session`

  If the session cannot proceed to the pulling phase, the session argument will be nil.
- ISyncSession can be used in different threads but is not itself thread-safe. It's up to you to ensure that you do not use it concurrently in multiple threads.
- The callback from `+ISyncSession beginSessionInBackgrounWithClient:entityNames:target:selector:` and `-ISyncSession prepareToPullChangesInBackgroundForEntityNames:target:selector:` can occur in any thread from which you have used the Sync Services API. There is no reliable way to know or determine which thread will be used.
- If a session cannot be started, the callback from `+ISyncSession beginSessionInBackgrounWithClient:entityNames:target:selector:` may be invoked with a nil session argument even before the call to `+beginSessionInBackgrounWithClient:entityNames:target:selector:` has returned.
- Relationships in records that are pulled from ISyncSession contain references to records which have been filtered or refused by the client. You will need to manually exclude these references, I'm afraid.
- Calling `-ISyncSession prepareToPullChangesForEntityNames:beforeDate:` again after it has returned YES will break ISyncSession. It's ok to call it again if it returns NO.
- ISyncSession may report false modifications to properties that you formatted when accepting a record. For example, if you truncate a contact's last name from "Smith" to "S", you will receive a change from ISyncSession setting the last name back to "Smith" when another client changes any other property on the record. You will need to re-format the property when you accept the record.
- ISyncSession keeps the same local ids for records when a client reports itself as reset using `-ISyncSession clientDidResetEntityNames:`. For example, if you accept a record with a local identifier "Foo" and on a subsequent sync report yourself as reset, that same record will be given back to you as "Foo". This behaviour may change in the future, so you should not rely on it.
- ISyncSession remembers the local record identifier for records that are removed by a client's filters. This prevents the client from being able to reuse the filtered record's local identifier, even though it appears to the client as if the record has been deleted.
- The snapshot returned from `-ISyncSession snapshotOfRecordsInTruth` is not invalidated when the session is cancelled or finished. It is, however, left in a "funny" state and may cause a crash if you continue using it.
- `-ISyncClient setFilters:` performs a logical OR instead of a logical AND on the filters. That is, a record will be given to the client in the pull phase if at least one filter accepts it. This contradicts the documentation and is a bug that will be fixed in a future release. For now, you should use a conjunction filter (`+ISyncFilter filterMatchingAllFilters:` and `+ISyncFilter filterMatchingAtLeastOneFilter:`) to get your desired behavior.
- ISyncSession does not perform a transitive closure over lost records (aka "cascading" loss). If a client reports a record as lost using `-ISyncSession clientLostRecordWithIdentifier:`, ISyncSession should traverse all "cascading delete" relationships and report the targets as lost as well. We will fix this in a future release; for now, you must perform this transitive closure manually (and we understand that may not always be possible).
- ISyncSession can push "clear" deltas for properties that were added when a client accepted a record but did not subsequently provide. For example, if a client accepts record A and adds a property Q in the formatted record, then pushes a change to X that does not include Q, ISyncSession should not issue a "clear" for Q.
- If your callback from `-ISyncSession prepareToPullChangesInBackgroundForEntityNames:target:selector:` is invoked with a nil session parameter, indicating the session has been cancelled, the session is left in a funny, quasi-cancelled state and will leak resources if no further action is taken. This can be remedied by invoking any method, such as `-ISyncSession cancelSyncing`, on the session from inside your callback or after your callback has returned.

### Schema Registration

- Sync Services allows for a couple of undocumented keys in the schema description:

  - "Parent" - a string on the entity description that identifies by name a relationship to the entity's "parent" entity. An entity is considered to be "owned" by its parent. This means that any conflicts on the entity will be displayed in the context of its parent; and any changes to the entity will be counted as changes against its parent for purposes of the Data Change Alert. For example, the Contact entity is the parent of the PhoneNumber entity and the PhoneNumber entity specifies the "contact" relationship as its parent relationship.
  - "ExcludeFromDataChangeAlert" - a boolean value on either an attribute, relationship or entity description. If true, changes to the attribute, relationship or entity as a whole will not be included in the Data Change Alert calculations.
- If a relationship is marked as "required" and has an inverse relationship, that inverse relationship must have a "cascading delete" delete rule. Sync Services requires this in order to maintain relationship integrity. This is not currently enforced when you register your schema but soon will be, at which time you will not be able to register non-compliant schemas.
- If a relationship is marked as a "parent" relationship and has an inverse relationship, that inverse relationship must have a "cascading delete" delete rule. Sync Services requires this in order to maintain relationship integrity. This is not currently enforced when you register your schema but soon will be, at which time you will not be able to register non-compliant schemas.
- If a relationship is marked as a "parent" relationship, it is implicitly "required" as well. For clarity, Sync Services will require this be stated explicitly in a schema in a future release and non-compliant schemas will be rejected.
- You should avoid using chains of "parent" relationships. That is, if an entity A has a parent relationship to an entity B, B should not itself have a parent relationship. This will confuse Sync Services and wreak havoc with the conflict resolver.
- You cannot specify a relationship as part of a dependent property set, only attributes.
- Sync Services doesn't do a very thorough job of cleaning up its records stores when schemas are modified or removed. It's about 95% of the way there, but you may experience some weird behaviour as you evolve your schema during development. To be on the safe side, you can manually remove your Sync Services data directory (`~/Library/Application Support/SyncServices/Local`). See the release note above for a caveat about removing the data directory while applications that use Sync Services are still running.
- Strongly-ordered relationships are not supported very well and are largely untested. Use them with caution and patience.
- Schema extensions to the canonical Contacts, Calendars and Bookmarks schemas cannot be synchronized through .Mac due to a limitation in the .Mac client. Your extensions can only be synchronized with other clients on the same computer. We will fix this in a future release.
- Sync Services does not check automatically for updated schema descriptions (eg. by stat()ing the file). Until such time, you must manually re-register your schemas when they change.
- You must not add new identity keys to an entity in a schema extension. This is currently accepted by Sync Services but causes unpredictable results and will be rejected in the future. Schemas that add identity keys in an extension will then be rejected.
- You must make sure always to specify an ExtensionName in a schema extension. Failure to do so will cause disastrous results.
- You must not specify relationships to entities in a different data class from the source. ie. you cannot create a relationship from CalendarEvent to Contact. This is currently accepted by Sync Services but will be rejected in a future release. Schemas that specify such relationships will then be rejected.
- It is possible to define a relationship on an entity that does not specify a target entity. In the absence of entity inheritance, this is necessary for some cases but should be avoided if possible.

### Client Registration

- You cannot register a client with an identifier that is longer than 255 characters. (You will get a "File name too long" exception.)
- You cannot automatically localized a client's display name. You must register a display name that has already been appropriately localized for the user's locale.
- Sync Services fails to find icons referenced in client and schema descriptions if they are moved. Bundles and other file references are tracked correctly.
- You cannot specify a relative path for a sync alert tool in the client's description file. You must specify an absolute path in the client description file, or use `-ISyncManager setSyncAlertToolPath:` to specify your client's sync alert tool.
- Clients must sync all "required" properties on an entity. Failure to do so will result in the client's records being rejected at runtime. In a future release, Sync Services will validate when a client is registered that it supports all required properties on an entity and will reject clients that do not. This may result in your client not being able to register.
- Sync Services does not check automatically for updated client descriptions (eg. by stat()ing the file). Until such time, you must manually re-register your clients when their descriptions change.
