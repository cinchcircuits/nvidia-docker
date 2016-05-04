Name: nvidia-docker
Version: 1
Release: 1
Summary: Nvidia turn of Docker thats supports using GPU's within docker.

Group: nvidia
License: nvidia
URL: http://www.nvidia.com/Download/index.aspx
Source0: nvidia-docker-1.tar.gz

BuildRequires:	gcc make kernel-headers
Requires:       gcc make kernel-headers bzip2

%description
Nvidia turn of Docker thats supports using GPU's within docker.

#%prep
#rm -Rf $RPM_BUILD_ROOT
#mkdir -p $RPM_BUILD_ROOT
#echo "Decompress source"
#cd $RPM_BUILD_ROOT;tar xfz %{SOURCE0} 
#echo "Finish decompress"

#%setup -q
#echo "setup"
#echo "#!/bin/sh" > $RPM_BUILD_ROOT/configure
#echo "exit 0" >> $RPM_BUILD_ROOT/configure
#chmod 755 $RPM_BUILD_ROOT/configure

#%configure
#echo "config"

%build
rm -Rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
echo "Decompress source"
cd $RPM_BUILD_ROOT;tar xfz %{SOURCE0} 
echo "Finish decompress"
echo "build"
cd $RPM_BUILD_ROOT/%{name}-%{version};make
cd $RPM_BUILD_ROOT/%{name}-%{version};make install destdir=/tmp
echo "end build"

%install
echo "install"
#%makeinstall INSTALLCMD='install -p' INSTALLMAN='install -p'
#mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/xinetd.d
#install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/xinetd.d/%{name}

#mkdir -p %{buildroot}/opt
#cp %{SOURCE0} %{buildroot}/opt/. 

%post 
echo "postinst"

%postun 
# Cleanup any files from opt that may be around
#rm -Rf /opt/NVIDIA-Linux-x86_64-%{version}

%files
#/opt/NVIDIA-Linux-x86_64-%{version}.tar.bz2

%changelog
* Wed May 4 2016 Michael Gregg <mgregg@nvidia.com> 1.1
- Initial RPM release
