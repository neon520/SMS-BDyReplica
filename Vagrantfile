# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

#	config.vm.define "localhost" do |l|
#		l.vm.hostname = "localhost"
#	end

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  	config.vm.box = "azure"
  	config.vm.provider :azure do |azure, override|
        # Mandatory Settings
      		azure.mgmt_certificate = File.expand_path(ENV['VA_CER_PEM'])
      		azure.mgmt_endpoint    = "https://management.core.windows.net"
      		azure.subscription_id = ENV['VA_SUB_AZURE']
      		azure.vm_name     = ENV['VA_VM_NAME']
      		#azure.cloud_service_name = ""
      		azure.vm_image    = "b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_2-LTS-amd64-server-20150506-en-us-30GB"
      		azure.vm_size     = "Small"
      		config.vm.box_url = "https://github.com/msopentech/vagrant-azure/raw/master/dummy.box"
        # Disable automatic box update checking. If you disable this, then
        # boxes will only be checked for updates when the user runs
        # `vagrant box outdated`. This is not recommended.
        # config.vm.box_check_update = false

        # Create a forwarded port mapping which allows access to a specific port
        # within the machine from a port on the host machine. In the example below,
        # accessing "localhost:8080" will access port 80 on the guest machine.
        # config.vm.network "forwarded_port", guest: 80, host: 8080

      		azure.vm_user = ENV['VA_USUARIO_AZURE'] # defaults to 'vagrant' if not provided
      		azure.vm_password = ENV['VA_PASS_AZURE']

      		azure.vm_location = "North Europe" # e.g., West US

      		azure.ssh_port             = "22"
	end
  config.ssh.username = ENV['VA_USUARIO_SSH']
  config.ssh.password = ENV['VA_PASS_SSH']
	config.vm.synced_folder ".", "/vagrant",disabled: true




  config.vm.provision "file", source: "VARIABLES_ENTORNO", destination: "/home/"+ENV['VA_USUARIO_AZURE']+"/VARIABLES_ENTORNO"
  config.vm.provision "shell", inline: "/home/"+ENV['VA_USUARIO_AZURE']+"/VARIABLES_ENTORNO "+ENV['VA_USUARIO_AZURE']
	config.vm.provision "ansible" do |ansible|
    #		 ansible.groups = {
    #      			'all' => ['default']
    #    		}
        #ansible.raw_arguments = ["-vvvv"]
    		ansible.force_remote_user = false
    		ansible.sudo = true
        #ansible.verbose = "vvv"
    		ansible.playbook = "ansible/configuracion_ansible.yml"
    #   	 	ansible.inventory_path = "ansible/vagrant_ansible_inventory"
    		#ansible.host_key_checking = false


        #ansible.playbook = ".vagrant/provisioners/ansible/inventory/webservice.yml"
        #ansible.inventory_path = ".vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory"
  end

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data
  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Define a Vagrant Push strategy for pushing to Atlas. Other push strategies
  # such as FTP and Heroku are also available. See the documentation at
  # https://docs.vagrantup.com/v2/push/atlas.html for more information.
  # config.push.define "atlas" do |push|
  #   push.app = "YOUR_ATLAS_USERNAME/YOUR_APPLICATION_NAME"
  # end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   sudo apt-get update
  #   sudo apt-get install -y apache2
  # SHELL
end
