from Modules import *
from Hardware.HardwareReportGenerator import generate_report
from UI.CLI import launch_cli

def main():
    config = load_config("config.plist")
    report = generate_report()
    
    modules = [
        ConfigValidator(config),
        FixAssistant(config),
        SleepSnapshotAnalyzer(config),
        USBMapValidator(config),
        GpuSpoofAssistant(config),
        NvramFixer(config),
        SmbiosOptimizer(config),
        AudioDeviceFixer(config),
        BluetoothFixer(config),
        NetworkDeviceFixer(config),
        StorageDeviceFixer(config),
        SecureBootFixer(config),
        RootPatchAssistant(config),
    ]
    
    for module in modules:
        module.run(report)
    
    FinalReportGenerator(modules).generate()

if __name__ == "__main__":
    launch_cli(main)
