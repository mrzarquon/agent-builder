%define _topdir     ~/packages
%define _tmppath    %{_topdir}/tmp
%define _prefix     /usr/local
%define _defaultdocdir    %{_prefix}/share/doc
%define _mandir     %{_prefix}/share/man

%define name      pe-agent
%define summary     Puppet Enterprise Agent packages
%define version     2.8.1
%define release     1
%define license     ASPL
%define group     Sales Engineering
%define vendor      Puppet Labs, Inc.
%define packager    mrzarquon
%define buildroot   %{_tmppath}/%{name}-root

Name:      %{name}
Version:   %{version}
Release:   %{release}
Packager:  %{packager}
Vendor:    %{vendor}
License:   %{license}
Summary:   %{summary}
Group:     %{group}
#Source:    %{source}
URL:       %{url}
Prefix:    %{_prefix}
Buildroot: %{buildroot}
Requires:  pe-puppet-enterprise-release = 2.8.1-1.pe.el6
Requires:  pe-ruby = 1.8.7.371-3.pe.el6
Requires:  pe-ruby-shadow = 1.4.1-8.pe.el6
Requires:  pe-rubygem-stomp = 1.2.3-1.1.9.pe.el6
Requires:  pe-rubygem-stomp-doc = 1.2.3-1.1.9.pe.el6
Requires:  pe-mcollective-common = 1.2.1-14.pe.el6
Requires:  pe-mcollective = 1.2.1-14.pe.el6
Requires:  pe-facter = 1.6.17-1.pe.el6
Requires:  pe-puppet = 2.7.21-7.pe.el6
Requires:  pe-augeas = 0.10.0-3.pe.el6
Requires:  pe-augeas-libs = 0.10.0-3.pe.el6
Requires:  pe-ruby-augeas = 0.4.1-1.pe.el6
Requires:  pe-ruby-ldap = 0.9.8-5.pe.el6
Requires:  pe-rubygem-hiera = 1.1.2-5.pe.el6
Requires:  pe-rubygem-hiera-puppet = 1.0.0-2.pe.el6

%description
This is a 
%files
