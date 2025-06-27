%define oname KDiskMark
Name: kdiskmark
Version: 3.2.0
Release: 1
Summary: Simple open-source disk benchmark tool for Linux distros

License: GPLv3+
URL: https://github.com/JonMagon/KDiskMark
Source0: https://github.com/JonMagon/KDiskMark/releases/download/%{version}/KDiskMark-%{version}-source.tar.gz

BuildRequires: pkgconfig(appstream-glib)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(ECM)
BuildRequires: cmake(PolkitQt6-1)
BuildRequires: desktop-file-utils
BuildRequires: qt6-qtbase-theme-gtk3
BuildRequires: cmake(VulkanHeaders)

Requires: fio
Requires: hicolor-icon-theme

%description
KDiskMark is an HDD and SSD benchmark tool with a very friendly graphical user
interface. KDiskMark with its presets and powerful GUI calls Flexible I/O
Tester and handles the output to provide an easy to view and interpret
comprehensive benchmark result.

%prep
%autosetup -n kdiskmark-%{version} -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libexecdir}/kdiskmark_helper
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/dbus-1/system-services/dev.jonmagon.kdiskmark.helperinterface.service
%{_datadir}/dbus-1/system.d/dev.jonmagon.kdiskmark.helperinterface.conf
%{_datadir}/polkit-1/actions/dev.jonmagon.kdiskmark.helper.policy
%{_datadir}/%{name}/
