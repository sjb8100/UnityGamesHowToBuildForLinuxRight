# UnityGamesHowToBuildForLinuxRight

Later versions of unity need GTK+ 3.4
http://www.linuxfromscratch.org/~thomasp/blfs-book-xsl/x/gtk3.html

https://forum.unity.com/threads/unity-rpm-package.460068/

https://gist.github.com/blaztinn/f92739cd23aceb6dcb9c1b0e47739cfc


http://allnightburger.com/installing-unity3d-on-fedora-24/

https://gist.github.com/bobmoff/8d5e1fc1e47b71bf33e53a2e55a62aff

Automatic updates are now supported in GNOME 3.30 via Flatpak in Fedora 29. Flatpak is a package management utility for distributing desktop applications on Linux.





xdg-app
now FlatPak / flatpak
$XDG_DATA_HOME/unity3d/Unity (local storage for the license information is stored in)
so this means unity editor is delivered via flatpak it would seem
https://wiki.archlinux.org/index.php/XDG_Base_Directory
 	Many game engines (Unity 3D, Unreal) follow the specification, but then individual game publishers hardcode the paths in Steam Auto-Cloud causing game-saves to sync to the wrong directory. 


option 1: vnc
https://github.com/sjb8100/docker-unity3d
https://forum.unity.com/threads/5-4-0p1-fails-to-launch-due-to-license.425277/#post-2941499

option 2:
https://github.com/GabLeRoux/unity3d-ci-example/blob/master/README.md



could work, first look at game for steam
https://github.com/flathub/com.valvesoftware.Steam


https://gitlab.com/gableroux/unity3d




