# Generated by rust2rpm 10
# * https://github.com/rust-lang-nursery/error-chain/issues/242
%bcond_with check
%global debug_package %{nil}

# https://github.com/rust-lang-nursery/error-chain/issues/267
%global __cargo_is_bin() false

%global crate error-chain

Name:           rust-%{crate}
Version:        0.12.1
Release:        5%{?dist}
Summary:        Error boilerplate library

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/error-chain
Source:         %{crates_source}
# Initial patched metadata
# * Update version_check to 0.9, https://github.com/rust-lang-nursery/error-chain/commit/f5417d2eb4f0f1398d61c9ecef948c37a073e563
Patch0:         error-chain-fix-metadata.diff
# Finish upgrade of version_check
Patch0001:      0001-Update-version_check-to-0.9.patch

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Yet another error boilerplate library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc CHANGELOG.md README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+backtrace-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+backtrace-devel %{_description}

This package contains library source intended for building other packages
which use "backtrace" feature of "%{crate}" crate.

%files       -n %{name}+backtrace-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+example_generated-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+example_generated-devel %{_description}

This package contains library source intended for building other packages
which use "example_generated" feature of "%{crate}" crate.

%files       -n %{name}+example_generated-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 12:09:51 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.1-4
- Update version_check to 0.9

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 20:11:52 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.1-2
- Regenerate

* Sun May 12 11:15:44 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.1-1
- Update to 0.12.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.0-3
- Run tests in infrastructure

* Fri Nov 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.0-2
- Adapt to new packaging

* Tue Jul 17 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.0-1
- Update to 0.12.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.0-2
- Rebuild for rust-packaging v5

* Wed Jan 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.0-1
- Initial package
