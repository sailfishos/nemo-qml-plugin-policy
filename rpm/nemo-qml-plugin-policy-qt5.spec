Name:       nemo-qml-plugin-policy-qt5

# >> macros
# << macros

Summary:    Resource policy plugin for Nemo Mobile
Version:    0.0.0
Release:    1
Group:      System/Libraries
License:    BSD
URL:        https://github.com/nemomobile/nemo-qml-plugin-policy
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(libresourceqt5)
Provides:   nemo-qml-plugins-policy-qt5

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5 

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre

# org.nemomobile.policy legacy import
mkdir -p %{buildroot}%{_libdir}/qt5/qml/org/nemomobile/policy/
ln -sf %{_libdir}/qt5/qml/Nemo/Policy/libnemopolicy.so %{buildroot}%{_libdir}/qt5/qml/org/nemomobile/policy/
sed 's/Nemo.Policy/org.nemomobile.policy/' < src/qmldir > %{buildroot}%{_libdir}/qt5/qml/org/nemomobile/policy/qmldir
%qmake_install

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%dir %{_libdir}/qt5/qml/Nemo/Policy
%{_libdir}/qt5/qml/Nemo/Policy/libnemopolicy.so
%{_libdir}/qt5/qml/Nemo/Policy/qmldir

# org.nemomobile.policy legacy import
%dir %{_libdir}/qt5/qml/org/nemomobile/policy
%{_libdir}/qt5/qml/org/nemomobile/policy/libnemopolicy.so
%{_libdir}/qt5/qml/org/nemomobile/policy/qmldir
# >> files
# << files
