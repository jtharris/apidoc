# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.define :docs do |docs|
    docs.vm.box = 'heroku/trusty64'
    docs.vm.box_url = 'https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box'
    docs.vm.network 'private_network', ip: '192.168.44.66'
    docs.vm.network 'forwarded_port', guest: 8000, host: 8000, auto_correct: true

    docs.vm.provision 'ansible' do |ansible|
      ansible.sudo = true
      ansible.playbook = 'provisioning/playbook.yml'
    end

    docs.vm.provider 'virtualbox' do |virtualbox|
      virtualbox.memory = 2048
      virtualbox.cpus = 4
    end
  end

end
