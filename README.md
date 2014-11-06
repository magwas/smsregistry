This program is a kind of sms receiver intended to maintain a voter registry based on cell phone numbers being relatively unique identifiers for persons IRL.

Functionality:

- Receive smses with gammu.
  An sms should contain an email address.
- If the sender of the SMS is new, then put the hash of the number and the email address into a database. Call a web service with the email address intended to create an account in a site.
- If the sender of the SMS is already in the database, change the email address. Call a web service with the old and new email address, intended to change the email address bound to the number.
- The database is periodically sent over using scp to provide backup and up to date voter registry.

 The number is concatenated with a secret, and hashed. This way the attacker have to know the secret to be able to brute force the number.

Requirements against the environment:
 It is written in python. For needed modules seethe code.
 The software depends on gammu.
 Notification about registration and email change should be made by the web services, to both the new and old email addresses.

Risk assessment:

 Building a user base based on cellphones is not unbeateable, just the least bad we could think of, with acceptably low barrier to entry (better than using email addressess or gogle/facebook/whatever logins).

 Ways to beat it:

- There are people with multiple cell phone numbers (but having more numbers is much harder than having more email accounts).
- There are subscriptions which can set A-number of smses

 SMS numbers are too short to meaningfully defend against a brute force attack, if the secret is known (could be obtained if the server running the software is hacked.)
