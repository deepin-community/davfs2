# davfs2 debconf translation to french
# Copyright (c) 2005-2006 Werner Baumann <wbaumann@users.sourceforge.net>
# This file is distributed under the same license as the davfs2 package.
#
msgid ""
msgstr ""
"Project-Id-Version: davfs2\n"
"Report-Msgid-Bugs-To: luciano@linux.org.ar\n"
"POT-Creation-Date: 2007-06-20 23:22+0200\n"
"PO-Revision-Date: 2006-05-29 19:14+0200\n"
"Last-Translator: Ivan Buresi <err747@free.fr>\n"
"Language-Team: French <debian-l10n-french@lists.debian.org>\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=utf-8\n"
"Content-Transfer-Encoding: 8bit\n"

#. Type: boolean
#. Description
#: ../templates:2001
msgid "Should unprivileged users be allowed to mount WebDAV resources?"
msgstr ""
"Autoriser les utilisateurs non privilégiés à monter des ressources WebDAV ?"

#. Type: boolean
#. Description
#: ../templates:2001
msgid ""
"The file /sbin/mount.davfs must have the SUID bit set if you want to allow "
"unprivileged (non-root) users to mount WebDAV resources."
msgstr ""
"Le fichier /sbin/mount.davfs doit avoir le bit SUID positionné pour "
"permettre aux utilisateurs non privilégiés de monter des ressources WebDAV."

#. Type: boolean
#. Description
#: ../templates:2001
msgid ""
"Choosing this option is discouraged for security reasons. If you choose it, "
"additional input will be required."
msgstr ""
"Cette option est déconseillée pour des raisons de sécurité. Si vous la "
"choisissez, des questions supplémentaires seront nécessaires."

#. Type: boolean
#. Description
#: ../templates:2001
msgid ""
"If you do not choose this option, only root will be allowed to mount WebDAV "
"resources. This can later be changed by running 'dpkg-reconfigure davfs2'."
msgstr ""
"Si vous ne choisissez pas cette option, seul le superutilisateur pourra "
"monter des ressources WebDAV. Il sera toujours possible de modifier ce choix "
"plus tard avec la commande « dpkg-reconfigure davfs2 »."

#. Type: string
#. Description
#: ../templates:3001
msgid "User running the mount.davfs daemon:"
msgstr "Identifiant qui exécutera le démon mount.davfs :"

#. Type: string
#. Description
#: ../templates:3001
msgid ""
"Once the davfs resource has been mounted, the daemon will drop the root "
"privileges and will run with an unprivileged user ID."
msgstr ""
"Lorsque la ressource WebDAV aura été montée, le démon abandonnera les "
"privilèges du superutilisateur et utilisera les privilèges d'un utilisateur "
"ordinaire."

#. Type: string
#. Description
#: ../templates:3001
msgid "Please choose which login name should be used by the daemon."
msgstr "Veuillez choisir l'identifiant à utiliser pour cela."

#. Type: string
#. Description
#: ../templates:4001
msgid "Group for users who will be allowed to mount WebDAV resources:"
msgstr "Groupe d'utilisateurs autorisés à monter des ressources WebDAV :"

#. Type: string
#. Description
#: ../templates:4001
msgid ""
"Mounting WebDAV resources creates a file in /var/run/mount.davfs. This "
"directory will be owned by the group specified here."
msgstr ""
"Le montage d'une ressource WebDAV créera un fichier dans le répertoire /var/"
"run/mount.davfs dont le propriétaire sera le groupe indiqué ici."

#. Type: boolean
#. Description
#: ../templates:5001
msgid "Do you want to create a new user?"
msgstr "Faut-il créer un nouvel identifiant ?"

#. Type: boolean
#. Description
#: ../templates:5001
msgid ""
"The \"${user_name}\" user does not exist on the system and will be created "
"if you choose this option."
msgstr ""
"L'identifiant « ${user_name} » n'existe pas sur le système. Si vous "
"choisissez cette option, il sera créé."

#. Type: boolean
#. Description
#: ../templates:6001
msgid "Do you want to create a new group?"
msgstr "Faut-il créer un nouveau groupe ?"

#. Type: boolean
#. Description
#: ../templates:6001
msgid ""
"The \"${group_name}\" group does not exist on the system and will be created "
"if you choose this option."
msgstr ""
"Le groupe « ${group_name} » n'existe pas sur le système. Si vous choisissez "
"cette option, il sera créé."

#. Type: note
#. Description
#: ../templates:7001
msgid "Unprivileged users allowed to mount WebDAV resources"
msgstr "Ressources WebDAV montables par des utilisateurs non privilégiés"

#. Type: note
#. Description
#. Please DO NOT translate variable names such as ${group_name}
#. and ${user_name}
#: ../templates:7001
msgid ""
"The \"${group_name}\" group and the \"${user_name}\" user will be used by "
"davfs2. All users who should be granted the right to mount WebDAV resources "
"should be added to the group \"${group_name}\" using the following command:"
msgstr ""
"Le groupe « ${group_name} » et l'utilisateur « ${user_name} » seront "
"utilisés par davfs2. Tous les utilisateurs que vous voulez autoriser à "
"monter des ressources WebDAV doivent être ajoutés au groupe "
"« ${group_name} » avec la commande :"

#. Type: note
#. Description
#: ../templates:7001
msgid "The following should also be added to /etc/fstab:"
msgstr "La ligne suivante doit être ajoutée au fichier /etc/fstab :"

#. Type: note
#. Description
#: ../templates:7001
msgid ""
"Additional options are available. Please read the mount.davfs man page for "
"more information."
msgstr ""
"Des options supplémentaires peuvent être utilisées le cas échéant. Veuillez "
"consulter la page de manuel de mount.davfs pour plus d'informations."
