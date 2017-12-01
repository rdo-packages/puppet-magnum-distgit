%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:                   puppet-magnum
Version:                11.3.2
Release:                1%{?dist}
Summary:                Puppet module for OpenStack Magnum
License:                ASL 2.0

URL:                    https://launchpad.net/puppet-magnum

Source0:                https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:              noarch

Requires:               puppet-inifile
Requires:               puppet-stdlib
Requires:               puppet-keystone
Requires:               puppet-openstacklib
Requires:               puppet-oslo
Requires:               puppet >= 2.7.0

%description
Installs and configures OpenStack Magnum.

%prep
%setup -q -n openstack-magnum-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/magnum/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/magnum/



%files
%{_datadir}/openstack-puppet/modules/magnum/


%changelog
* Fri Dec 01 2017 RDO <dev@lists.rdoproject.org> 11.3.2-1
- Update to 11.3.2

* Sun Oct 08 2017 rdo-trunk <javier.pena@redhat.com> 11.3.1-1
- Update to 11.3.1

* Fri Aug 25 2017 Alfredo Moralejo <amoralej@redhat.com> 11.3.0-1
- Update to 11.3.0



