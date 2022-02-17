using System;
using System.Diagnostics;
using System.IO;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Media;

namespace SeaLevelRise
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        String assetsFolder = "../../../../assets/";
        public MainWindow()
        {
            InitializeComponent();
        }

        private void Slider_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {
            double year = slYear.Value;
        }

        private void clickedGenerate(object sender, RoutedEventArgs e)
        {

            Result.Source = (ImageSource)new ImageSourceConverter().ConvertFrom(assetsFolder + "waiting.png");

            if (File.Exists("../../../../output.png"))
            {
                File.Delete("../../../../output.png");
            }

            String focus = "";
            String colorbar = "";

            if ((bool)Focus.IsChecked)
            {
                focus = " --f ";
            }
            if ((bool)Colorbar.IsChecked == false)
            {
                colorbar = " --nc ";
            }

            String dataset = " " + ((ComboBoxItem)Dataset.SelectedItem).Name.ToString() + " ";
            String scenario = " " + ((ComboBoxItem)Scenario.SelectedItem).Name.ToString().TrimStart('r', 'c', 'p') + " ";
            String year = " --y=" + slYear.Value.ToString();

            String command = "/C cd ../../../../script/ && python3 main.py --sl " + dataset + scenario + focus + colorbar + year;

            
            /*
             * Displays the console for debugging
            ProcessStartInfo cmdsi = new ProcessStartInfo("cmd.exe");
            cmdsi.Arguments = command;
            Process cmd = Process.Start(cmdsi);
            cmd.WaitForExit();
            */

            
            System.Diagnostics.Process process = new System.Diagnostics.Process();
            System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo();
            startInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
            startInfo.FileName = "cmd.exe";
            startInfo.Arguments = command;
            process.StartInfo = startInfo;
            process.Start();
            process.WaitForExit();
            

            Result.Source = (ImageSource)new ImageSourceConverter().ConvertFrom("../../../../output.png");
        }
    }
}



