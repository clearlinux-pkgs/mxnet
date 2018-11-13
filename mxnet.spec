#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x91052D922E28A38F (zhasheng@apache.org)
#
Name     : mxnet
Version  : 1.3.0
Release  : 2
URL      : https://github.com/apache/incubator-mxnet/releases/download/1.3.0/apache-mxnet-src-1.3.0-incubating.tar.gz
Source0  : https://github.com/apache/incubator-mxnet/releases/download/1.3.0/apache-mxnet-src-1.3.0-incubating.tar.gz
Source99 : https://github.com/apache/incubator-mxnet/releases/download/1.3.0/apache-mxnet-src-1.3.0-incubating.tar.gz.asc
Summary  : 'Perl interface to MXNet Gluon ModelZoo'
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause BSD-3-Clause-LBNL MIT NCSA
Requires: mxnet-license = %{version}-%{release}
Requires: mxnet-python = %{version}-%{release}
Requires: mxnet-python3 = %{version}-%{release}
Requires: PyYAML
Requires: decorator
Requires: h5py
Requires: nose
Requires: numpy
Requires: onnx
Requires: pylint
Requires: python-mock
Requires: requests
Requires: scipy
BuildRequires : PyYAML
BuildRequires : Vulkan-Headers-dev Vulkan-Loader-dev Vulkan-Tools
BuildRequires : apache-spark
BuildRequires : beignet-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-cpan
BuildRequires : buildreq-distutils3
BuildRequires : cmake
BuildRequires : curl-dev
BuildRequires : decorator
BuildRequires : dmlc-core-dev
BuildRequires : doxygen
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : googletest-dev
BuildRequires : mesa-dev
BuildRequires : numpy
BuildRequires : onnx
BuildRequires : opencv-dev
BuildRequires : openjdk9-dev
BuildRequires : openssl-dev
BuildRequires : perl
BuildRequires : pkg-config
BuildRequires : pkgconfig(jemalloc)
BuildRequires : pkgconfig(libffi)
BuildRequires : protobuf-dev
BuildRequires : python3
BuildRequires : python3-dev
Patch1: 0001-Use-system-mkldnn.patch
Patch2: 0002-Use-system-dmlc-core.patch
Patch3: 0003-Put-.so-in-python-libdir.patch

%description
This archive contains the distribution AI-MXNet-Gluon-ModelZoo,
version 1.32:
Perl interface to MXNet Gluon ModelZoo, a collection of pretrained machine learning models for computer vision.

%package dev
Summary: dev components for the mxnet package.
Group: Development
Provides: mxnet-devel = %{version}-%{release}

%description dev
dev components for the mxnet package.


%package license
Summary: license components for the mxnet package.
Group: Default

%description license
license components for the mxnet package.


%package python
Summary: python components for the mxnet package.
Group: Default
Requires: mxnet-python3 = %{version}-%{release}

%description python
python components for the mxnet package.


%package python3
Summary: python3 components for the mxnet package.
Group: Default
Requires: python3-core

%description python3
python3 components for the mxnet package.


%prep
%setup -q -n apache-mxnet-src-1.3.0-incubating
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542149521
mkdir -p clr-build
pushd clr-build
%cmake .. -DUSE_CUDA=OFF -DUSE_MKLDNN=0 -DUSE_BLAS=openblas
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1542149521
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mxnet
cp 3rdparty/cub/LICENSE.TXT %{buildroot}/usr/share/package-licenses/mxnet/3rdparty_cub_LICENSE.TXT
cp 3rdparty/dlpack/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/3rdparty_dlpack_LICENSE
cp 3rdparty/dmlc-core/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/3rdparty_dmlc-core_LICENSE
cp 3rdparty/googletest/googlemock/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/3rdparty_googletest_googlemock_LICENSE
cp 3rdparty/googletest/googlemock/scripts/generator/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/3rdparty_googletest_googlemock_scripts_generator_LICENSE
cp 3rdparty/googletest/googletest/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/3rdparty_googletest_googletest_LICENSE
cp 3rdparty/mkldnn/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/3rdparty_mkldnn_LICENSE
cp 3rdparty/mkldnn/src/cpu/xbyak/COPYRIGHT %{buildroot}/usr/share/package-licenses/mxnet/3rdparty_mkldnn_src_cpu_xbyak_COPYRIGHT
cp 3rdparty/mkldnn/tests/gtests/gtest/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/3rdparty_mkldnn_tests_gtests_gtest_LICENSE
cp 3rdparty/mshadow/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/3rdparty_mshadow_LICENSE
cp 3rdparty/onnx-tensorrt/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/3rdparty_onnx-tensorrt_LICENSE
cp 3rdparty/onnx-tensorrt/third_party/onnx/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/3rdparty_onnx-tensorrt_third_party_onnx_LICENSE
cp 3rdparty/onnx-tensorrt/third_party/onnx/third_party/benchmark/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/3rdparty_onnx-tensorrt_third_party_onnx_third_party_benchmark_LICENSE
cp 3rdparty/onnx-tensorrt/third_party/onnx/third_party/pybind11/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/3rdparty_onnx-tensorrt_third_party_onnx_third_party_pybind11_LICENSE
cp 3rdparty/onnx-tensorrt/third_party/onnx/third_party/pybind11/tools/clang/LICENSE.TXT %{buildroot}/usr/share/package-licenses/mxnet/3rdparty_onnx-tensorrt_third_party_onnx_third_party_pybind11_tools_clang_LICENSE.TXT
cp 3rdparty/openmp/LICENSE.txt %{buildroot}/usr/share/package-licenses/mxnet/3rdparty_openmp_LICENSE.txt
cp 3rdparty/openmp/testsuite/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/3rdparty_openmp_testsuite_LICENSE
cp 3rdparty/ps-lite/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/3rdparty_ps-lite_LICENSE
cp 3rdparty/tvm/HalideIR/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/3rdparty_tvm_HalideIR_LICENSE
cp 3rdparty/tvm/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/3rdparty_tvm_LICENSE
cp 3rdparty/tvm/dlpack/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/3rdparty_tvm_dlpack_LICENSE
cp 3rdparty/tvm/dmlc-core/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/3rdparty_tvm_dmlc-core_LICENSE
cp LICENSE %{buildroot}/usr/share/package-licenses/mxnet/LICENSE
cp NOTICE %{buildroot}/usr/share/package-licenses/mxnet/NOTICE
cp contrib/clojure-package/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/contrib_clojure-package_LICENSE
cp cpp-package/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/cpp-package_LICENSE
cp docker/Dockerfiles/License.md %{buildroot}/usr/share/package-licenses/mxnet/docker_Dockerfiles_License.md
cp example/gluon/tree_lstm/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/example_gluon_tree_lstm_LICENSE
cp example/rcnn/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/example_rcnn_LICENSE
cp python/mxnet/contrib/onnx/mx2onnx/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/python_mxnet_contrib_onnx_mx2onnx_LICENSE
cp scala-package/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/scala-package_LICENSE
cp src/operator/contrib/ctc_include/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/src_operator_contrib_ctc_include_LICENSE
cp src/operator/contrib/ctc_include/contrib/moderngpu/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/src_operator_contrib_ctc_include_contrib_moderngpu_LICENSE
pushd clr-build
%make_install
popd
## install_append content
pushd python
eu-strip $(pwd)/../clr-build/libmxnet.so
MXNET_LIBRARY_PATH=$(pwd)/../clr-build/libmxnet.so python3 -tt setup.py build install --root=%{buildroot}
popd
## install_append end

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
%exclude /usr/include/gtest/gtest-death-test.h
%exclude /usr/include/gtest/gtest-message.h
%exclude /usr/include/gtest/gtest-param-test.h
%exclude /usr/include/gtest/gtest-param-test.h.pump
%exclude /usr/include/gtest/gtest-printers.h
%exclude /usr/include/gtest/gtest-spi.h
%exclude /usr/include/gtest/gtest-test-part.h
%exclude /usr/include/gtest/gtest-typed-test.h
%exclude /usr/include/gtest/gtest.h
%exclude /usr/include/gtest/gtest_pred_impl.h
%exclude /usr/include/gtest/gtest_prod.h
%exclude /usr/include/gtest/internal/custom/gtest-port.h
%exclude /usr/include/gtest/internal/custom/gtest-printers.h
%exclude /usr/include/gtest/internal/custom/gtest.h
%exclude /usr/include/gtest/internal/gtest-death-test-internal.h
%exclude /usr/include/gtest/internal/gtest-filepath.h
%exclude /usr/include/gtest/internal/gtest-internal.h
%exclude /usr/include/gtest/internal/gtest-linked_ptr.h
%exclude /usr/include/gtest/internal/gtest-param-util-generated.h
%exclude /usr/include/gtest/internal/gtest-param-util-generated.h.pump
%exclude /usr/include/gtest/internal/gtest-param-util.h
%exclude /usr/include/gtest/internal/gtest-port-arch.h
%exclude /usr/include/gtest/internal/gtest-port.h
%exclude /usr/include/gtest/internal/gtest-string.h
%exclude /usr/include/gtest/internal/gtest-tuple.h
%exclude /usr/include/gtest/internal/gtest-tuple.h.pump
%exclude /usr/include/gtest/internal/gtest-type-util.h
%exclude /usr/include/gtest/internal/gtest-type-util.h.pump
%exclude /usr/include/omp.h
%exclude /usr/lib/libgomp.so
%exclude /usr/lib/libgtest.so
%exclude /usr/lib/libgtest_main.so
%exclude /usr/lib/libiomp5.so
%exclude /usr/lib/libomp.so
/usr/include/mxnet/base.h
/usr/include/mxnet/c_api.h
/usr/include/mxnet/c_predict_api.h
/usr/include/mxnet/engine.h
/usr/include/mxnet/executor.h
/usr/include/mxnet/graph_attr_types.h
/usr/include/mxnet/imperative.h
/usr/include/mxnet/io.h
/usr/include/mxnet/kvstore.h
/usr/include/mxnet/ndarray.h
/usr/include/mxnet/op_attr_types.h
/usr/include/mxnet/operator.h
/usr/include/mxnet/operator_util.h
/usr/include/mxnet/resource.h
/usr/include/mxnet/rtc.h
/usr/include/mxnet/storage.h
/usr/include/mxnet/tensor_blob.h
/usr/lib64/libmxnet.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mxnet/3rdparty_cub_LICENSE.TXT
/usr/share/package-licenses/mxnet/3rdparty_dlpack_LICENSE
/usr/share/package-licenses/mxnet/3rdparty_dmlc-core_LICENSE
/usr/share/package-licenses/mxnet/3rdparty_googletest_googlemock_LICENSE
/usr/share/package-licenses/mxnet/3rdparty_googletest_googlemock_scripts_generator_LICENSE
/usr/share/package-licenses/mxnet/3rdparty_googletest_googletest_LICENSE
/usr/share/package-licenses/mxnet/3rdparty_mkldnn_LICENSE
/usr/share/package-licenses/mxnet/3rdparty_mkldnn_src_cpu_xbyak_COPYRIGHT
/usr/share/package-licenses/mxnet/3rdparty_mkldnn_tests_gtests_gtest_LICENSE
/usr/share/package-licenses/mxnet/3rdparty_mshadow_LICENSE
/usr/share/package-licenses/mxnet/3rdparty_onnx-tensorrt_LICENSE
/usr/share/package-licenses/mxnet/3rdparty_onnx-tensorrt_third_party_onnx_LICENSE
/usr/share/package-licenses/mxnet/3rdparty_onnx-tensorrt_third_party_onnx_third_party_benchmark_LICENSE
/usr/share/package-licenses/mxnet/3rdparty_onnx-tensorrt_third_party_onnx_third_party_pybind11_LICENSE
/usr/share/package-licenses/mxnet/3rdparty_onnx-tensorrt_third_party_onnx_third_party_pybind11_tools_clang_LICENSE.TXT
/usr/share/package-licenses/mxnet/3rdparty_openmp_LICENSE.txt
/usr/share/package-licenses/mxnet/3rdparty_openmp_testsuite_LICENSE
/usr/share/package-licenses/mxnet/3rdparty_ps-lite_LICENSE
/usr/share/package-licenses/mxnet/3rdparty_tvm_HalideIR_LICENSE
/usr/share/package-licenses/mxnet/3rdparty_tvm_LICENSE
/usr/share/package-licenses/mxnet/3rdparty_tvm_dlpack_LICENSE
/usr/share/package-licenses/mxnet/3rdparty_tvm_dmlc-core_LICENSE
/usr/share/package-licenses/mxnet/LICENSE
/usr/share/package-licenses/mxnet/NOTICE
/usr/share/package-licenses/mxnet/contrib_clojure-package_LICENSE
/usr/share/package-licenses/mxnet/cpp-package_LICENSE
/usr/share/package-licenses/mxnet/docker_Dockerfiles_License.md
/usr/share/package-licenses/mxnet/example_gluon_tree_lstm_LICENSE
/usr/share/package-licenses/mxnet/example_rcnn_LICENSE
/usr/share/package-licenses/mxnet/python_mxnet_contrib_onnx_mx2onnx_LICENSE
/usr/share/package-licenses/mxnet/scala-package_LICENSE
/usr/share/package-licenses/mxnet/src_operator_contrib_ctc_include_LICENSE
/usr/share/package-licenses/mxnet/src_operator_contrib_ctc_include_contrib_moderngpu_LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
