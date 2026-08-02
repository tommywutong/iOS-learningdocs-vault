---
title: Repositories Organizer Help
apple_id: TP40010350
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/recipes/xcode_help-repositories_organizer/articles/PullingUpdatesfromaRemoteRepository.html
archived_at: '2026-07-18T02:39:13.358850Z'
---
> 导航：[总目录](../../README.md) · [recipes](../../_indexes/recipes.md) · [Repositories Organizer Help](Repositories%20Organizer%20Help%20%28Legacy%29.md)



# Pulling Changes from a Remote Git Repository

Use a pull operation to update local files with changes from a shared or remote Git repository to ensure that your local repository is up to date.

![bullet](../../_unindexed/Resources/1282/Images/task_2x.png)To pull changes from a remote Git repository

1. Choose File > Source Control > Pull.
2. In the Pull dialog, select a file in the navigation pane.
3. Select a difference to reconcile by clicking its indicator.
4. Use the left and right buttons to specify how the difference is to be reconciled.
5. After reconciling all differences, click Pull to complete the operation.

   The illustration shows the Pull dialog, with a conflict selected.

   ![../art/repositories_pull_lr.png](attachments/art/repositories_pull_lr.png)

Before you can push changes in your local repository to a shared repository, Git requires a pull operation, in which you reconcile differences between the two repositories. This reconciliation helps prevent your accidentally modifying or undoing other developers’ changes.

You need to save changes you’ve made and commit them to your local repository before pulling changes from the shared repository.

In the Pull dialog, you select a difference by clicking the indicator between the two files. You then click one of the four buttons at the bottom to choose how that difference is to be reconciled. The indicator updates to reflect your choice.

A difference in which a line of code has been changed in both versions of the file is considered a conflict, and its indicator is a question mark. You can’t complete the pull operation until you specify how to resolve all conflicts.

If you wish, you can edit the local revision of the file in the Pull dialog to reconcile any differences not handled by the four button choices.

In busy times , multiple developers may attempt to submit changes to the shared repository at the same time. If another developer’s submission completes before yours, Xcode informs you that you must first perform a new pull operation. In larger organizations, particularly just prior to a product release, you may find that you have to pull changes more than once.

After the pull operation, you have to commit the changes files in your local repository that are updated by the pull operation.

### Related Articles

- About the Organizer Window
- [Committing Files to a Repository](Committing%20Files%20to%20a%20Repository.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydgnjqfvbuqobnknltc)
- [Merging Two Branches](Merging%20Two%20Branches.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydgnjqfvbuqmjqfvjvomi)
