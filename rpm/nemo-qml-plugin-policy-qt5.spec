Name:       nemo-qml-plugin-policy-qt5

Summary:    Resource policy plugin for Nemo Mobile
Version:    0.1.4
Release:    1
License:    BSD
URL:        https://github.com/sailfishos/nemo-qml-plugin-policy
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(libresourceqt5)
Provides:   nemo-qml-plugins-policy-qt5

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build
%qmake5 

%make_build

%install

# org.nemomobile.policy legacy import
mkdir -p %{buildroot}%{_libdir}/qt5/qml/org/nemomobile/policy/
ln -sf %{_libdir}/qt5/qml/Nemo/Policy/libnemopolicy.so %{buildroot}%{_libdir}/qt5/qml/org/nemomobile/policy/
sed 's/Nemo.Policy/org.nemomobile.policy/' < src/qmldir > %{buildroot}%{_libdir}/qt5/qml/org/nemomobile/policy/qmldir
%qmake_install

%files
%defattr(-,root,root,-)
%license LICENSE.BSD
%dir %{_libdir}/qt5/qml/Nemo/Policy
%{_libdir}/qt5/qml/Nemo/Policy/libnemopolicy.so
%{_libdir}/qt5/qml/Nemo/Policy/plugins.qmltypes
%{_libdir}/qt5/qml/Nemo/Policy/qmldir

# org.nemomobile.policy legacy import
%dir %{_libdir}/qt5/qml/org/nemomobile/policy
%{_libdir}/qt5/qml/org/nemomobile/policy/libnemopolicy.so
%{_libdir}/qt5/qml/org/nemomobile/policy/qmldir
