Name: kdiskmark
Version: 2.0.0
Release: 1
Summary: Simple open-source disk benchmark tool for Linux distros

License: GPLv3+
URL: https://github.com/JonMagon/KDiskMark
Source0: https://github.com/JonMagon/KDiskMark/archive/%{version}/%{name}-%{version}.tar.gz
Patch0: https://github.com/JonMagon/KDiskMark/pull/32.patch#/fix-appdata-manifest-typo.patch


BuildRequires: libappstream-glib8
BuildRequires: pkgconfig(appstream-glib)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(ECM)
BuildRequires: desktop-file-utils

Requires: fio
Requires: hicolor-icon-theme

%description
KDiskMark is an HDD and SSD benchmark tool with a very friendly graphical user
interface. KDiskMark with its presets and powerful GUI calls Flexible I/O
Tester and handles the output to provide an easy to view and interpret
comprehensive benchmark result.


%prep
%autosetup -n KDiskMark-%{version} -p1


%build
%cmake
%make_build


%install
%make_install -C build


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/%{name}/
