Name: kdiskmark
Version: 2.0.0
Release: 1%{?dist}
Summary: Simple open-source disk benchmark tool for Linux distros

License: GPLv3+
URL: https://github.com/JonMagon/KDiskMark
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0: https://github.com/JonMagon/KDiskMark/pull/32.patch#/fix-appdata-manifest-typo.patch

# For next releases
# BuildRequires: libappstream-glib

BuildRequires: cmake(Qt5Core) >= 5.9
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: desktop-file-utils

Requires: fio%{?_isa} >= 3.1
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
%cmake_build


%install
%cmake_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/%{name}/


%changelog
* Sat Oct 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.0-1
- build(update): 2.0.0

* Wed Oct  7 20:58:18 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.2-2
- build: remove 20px icon version

* Sun Oct  4 13:55:31 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.2-1
- Initial package
