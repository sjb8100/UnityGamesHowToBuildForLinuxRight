# included_files are autodetected dependencies that are provided by this package
%global included_files ^libcef\.so(.*)$\|libCg\.so(.*)$\|libfreeimage\.so\.3(.*)$\|libglslang\.so(.*)$\|libispc_texcomp\.so(.*)$\|libmain\.so(.*)$\|libmono\.so(.*)$\|libQt5Core\.so\.5(.*)$\|libQt5DBus\.so\.5(.*)$\|libQt5Gui\.so\.5(.*)$\|libQt5Network\.so\.5(.*)$\|libQt5Widgets\.so\.5(.*)$\|libQt5Xml\.so\.5(.*)$\|libTextureConverter\.so(.*)$\|libumbraoptimizer64\.so(.*)$\|osgi(.*)$

# missing_deps are autodetected dependencies that I was unable to find a package to provide.
%global missing_deps ^ld-linux-x86-64\.so\.2(.*)$\|ld-linux\.so\.3(.*)$\|libcapi-appfw-app-common\.so\.0(.*)$\|libcapi-appfw-app-control\.so\.0(.*)$\|libcapi-appfw-application\.so\.0(.*)$\|libcapi-base-common\.so\.0(.*)$\|libcapi-location-manager\.so\.0(.*)$\|libcapi-media-audio-io\.so\.0(.*)$\|libcapi-media-camera\.so\.0(.*)$\|libcapi-media-player\.so\.0(.*)$\|libcapi-media-sound-manager\.so\.0(.*)$\|libcapi-system-device\.so\.0(.*)$\|libcapi-system-info\.so\.0(.*)$\|libcapi-system-sensor\.so\.0(.*)$\|libcapi-system-system-settings\.so\.0(.*)$\|libcrypto\.so\.1\.0\.0(.*)$\|libdlog\.so\.0(.*)$\|libefl-extension\.so\.0(.*)$\|liblog\.so(.*)$\|rtld(.*)$\|/usr/local/bin/python(.*)$

# deps_with_packages excludes all dependencies that are specified under Requires.
%global deps_with_packages ^bash(.*)$\|bash(.*)$\|rhythmbox(.*)$\|cairo(.*)$\|libcap(.*)$\|glibc-devel(.*)$\|cups-libs(.*)$\|libcurl(.*)$\|dbus-libs(.*)$\|glibc-devel(.*)$\|expat(.*)$\|fontconfig(.*)$\|freetype(.*)$\|GConf2(.*)$\|gdk-pixbuf2(.*)$\|gtk2(.*)$\|glib2(.*)$\|glib2(.*)$\|mesa-libGL(.*)$\|mesa-libGLU(.*)$\|glib2(.*)$\|gtk2(.*)$\|libICE(.*)$\|glibc-devel(.*)$\|nspr(.*)$\|nss(.*)$\|nss-util(.*)$\|pango(.*)$\|pango(.*)$\|nspr(.*)$\|nss(.*)$\|libSM(.*)$\|libstdc++(.*)$\|libX11(.*)$\|libX11(.*)$\|libxcb(.*)$\|libXcomposite(.*)$\|libXcursor(.*)$\|libXdamage(.*)$\|libXext(.*)$\|libXfixes(.*)$\|libXi(.*)$\|libXrandr(.*)$\|libXrender(.*)$\|libXtst(.*)$\|zlib(.*)$\|coreutils(.*)$\|perl(.*)$\|python(.*)$\|python(.*)$\|alsa-lib(.*)$\|glibc(.*)$\|glibc(.*)$\|libgcc(.*)$\|glibc(.*)$\|glibc(.*)$\|glibc(.*)$\|glibc(.*)$\|efl(.*)$\|efl(.*)$\|chromium-libs(.*)$\|libglvnd-devel(.*)$\|efl(.*)$\|efl(.*)$\|chromium-libs(.*)$\|libglvnd-devel(.*)$\|libpng12(.*)$\|postgresql-libs(.*)$\|SDL(.*)$\|SDL_image(.*)$\|SDL_mixer(.*)$\|SDL_net(.*)$\|SDL_ttf(.*)$\|compat-gcc-34-c++(.*)$\|gcc-c++(.*)$\|libstdc++-devel(.*)$\|zlib-devel(.*)$\|npm(.*)$\|

# __requires_exclude compiles the 3 lists above into 1 and excludes them from the RPM's dependencies.
%global __requires_exclude %{deps_with_packages}\|%{included_files}\|%{missing_deps}

%define extractpath       /usr/share
%define installpath       /usr/share/unity-editor
%define icon              /unity-editor-icon.png

Name:           unity-editor
Version:        5.5.2f1
Release:        1%{?dist}
Summary:        Unity development platform

License:        Proprietary
URL:            https://unity3d.com/

Source0:        http://beta.unity3d.com/download/e06241adb51f/unity-editor-installer-5.5.2xf1Linux.sh

BuildRequires:  ImageMagick chrpath
Requires:       alsa-lib, bash, cairo, chromium-libs, compat-gcc-34-c++, coreutils, cups-libs, dbus-libs, efl, expat, fontconfig, freetype, gcc-c++, GConf2, gdk-pixbuf2, glib2, glibc, glibc-devel, gtk2, libcap, libcurl, libgcc, libglvnd-devel, libICE, libpng12, libSM, libstdc++, libstdc++-devel, libX11, libxcb, libXcomposite, libXcursor, libXdamage, libXext, libXfixes, libXi, libXrandr, libXrender, libXtst, mesa-libGL, mesa-libGLU, npm, nspr, nss, nss-util, pango, perl, postgresql-libs, python, rhythmbox, SDL, SDL_image, SDL_mixer, SDL_net, SDL_ttf, zlib, zlib-devel



%description
Unity is a cross-platform game engine developed by Unity Technologies and used to develop video games for PC, consoles, mobile devices and websites. First announced only for OS X, at Apple's Worldwide Developers Conference in 2005, it has since been extended to target 27 platforms.

%prep

%build

%install
mkdir %{buildroot}%{extractpath}/ -p
# Extract the files from the Platform-Agnostic Installer
tail -n+`awk '/^__ARCHIVE_BEGINS_HERE__/ {print NR + 1; exit 0; }' %{SOURCE0}` %{SOURCE0} | tar xj -C "%{buildroot}%{extractpath}/"
mv %{buildroot}%{extractpath}/unity-editor-5.5.2xf1Linux %{buildroot}%{installpath}

for size in 16 24 32 48 64 96 128 192 256 512
do
  mkdir -p %{buildroot}/usr/share/icons/hicolor/${size}x${size}/apps/
  convert %{buildroot}%{installpath}/unity-editor-icon.png -resize ${size}x${size} %{buildroot}/usr/share/icons/hicolor/${size}x${size}/apps/unity-editor-icon.png
done
for size in 64 128
do
  mkdir -p %{buildroot}/usr/share/app-info/icons/fedora/${size}x${size}/
  convert %{buildroot}%{installpath}/unity-editor-icon.png -resize ${size}x${size} %{buildroot}/usr/share/app-info/icons/fedora/${size}x${size}/unity-editor-icon.png
done
rm %{buildroot}%{installpath}/unity-editor-icon.png

mkdir -p %{buildroot}/usr/share/applications
mv %{buildroot}%{installpath}/unity-editor.desktop %{buildroot}/usr/share/applications/
mv %{buildroot}%{installpath}/unity-monodevelop.desktop %{buildroot}/usr/share/applications/
sed -i 's|/opt/Unity|%{installpath}|g' %{buildroot}/usr/share/applications/unity-editor.desktop
sed -i 's|/opt/Unity|%{installpath}|g' %{buildroot}/usr/share/applications/unity-monodevelop.desktop

mkdir -p %{buildroot}%{_bindir}/
ln -s %{installpath}/Editor/Unity %{buildroot}/usr/bin/unity-editor

#Delete rpaths
chrpath --delete %{buildroot}%{installpath}/Editor/BugReporter/platforms/libqxcb.so
chrpath --delete %{buildroot}%{installpath}/Editor/BugReporter/libQt5Xml.so.5
chrpath --delete %{buildroot}%{installpath}/Editor/BugReporter/libQt5Widgets.so.5
chrpath --delete %{buildroot}%{installpath}/Editor/BugReporter/imageformats/libqico.so
chrpath --delete %{buildroot}%{installpath}/Editor/BugReporter/imageformats/libqgif.so
chrpath --delete %{buildroot}%{installpath}/Editor/BugReporter/libQt5DBus.so.5
chrpath --delete %{buildroot}%{installpath}/Editor/BugReporter/libQt5Gui.so.5
chrpath --delete %{buildroot}%{installpath}/Editor/BugReporter/libQt5Network.so.5
chrpath --delete %{buildroot}%{installpath}/Editor/BugReporter/libQt5PrintSupport.so.5

chrpath --delete %{buildroot}%{installpath}/Editor/Data/PlaybackEngines/TizenPlayer/Device/TizenDevelopmentPlayer/TizenPlayer
chrpath --delete %{buildroot}%{installpath}/Editor/Data/PlaybackEngines/TizenPlayer/Device/TizenPlayer/TizenPlayer
chrpath --delete %{buildroot}%{installpath}/Editor/Data/PlaybackEngines/TizenPlayer/Emulator/TizenDevelopmentPlayer/TizenPlayer
chrpath --delete %{buildroot}%{installpath}/Editor/Data/PlaybackEngines/TizenPlayer/Emulator/TizenPlayer/TizenPlayer

chrpath --delete %{buildroot}%{installpath}/Editor/Data/PlaybackEngines/STVPlayer/STVPlayer/libmain_STANDARD_15.so
chrpath --delete %{buildroot}%{installpath}/Editor/Data/PlaybackEngines/STVPlayer/STVPlayer/game_STANDARD_15.so
chrpath --delete %{buildroot}%{installpath}/Editor/Data/PlaybackEngines/STVPlayer/STVDevelopmentPlayer/libmain_STANDARD_15.so
chrpath --delete %{buildroot}%{installpath}/Editor/Data/PlaybackEngines/STVPlayer/STVDevelopmentPlayer/game_STANDARD_15.so

chrpath --delete %{buildroot}%{installpath}/Editor/Data/Tools/FSBTool/libvorbis.so
chrpath --delete %{buildroot}%{installpath}/Editor/Data/Tools/FSBTool/libvorbisfile.so
chrpath --delete %{buildroot}%{installpath}/Editor/Data/Tools/FSBTool/libvorbis.so.0
 
%files
%defattr(-,root,root,-)
%{installpath}
/usr/share/icons/hicolor/*
/usr/share/app-info/icons/fedora/*
/usr/share/applications/*
/usr/bin/unity-editor
# chrome-sandbox requires this: https://code.google.com/p/chromium/wiki/LinuxSUIDSandbox
%attr(4755,root,root) %{installpath}/Editor/chrome-sandbox
