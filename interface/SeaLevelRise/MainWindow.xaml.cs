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
        const String assetsFolder = "../../../../assets/";

        public MainWindow()
        {
            InitializeComponent();
        }

        private void Slider_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {
            _ = slYear.Value;
        }

        private void ScenarioSelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            //if (Scenario.SelectedItem == rcpall) ((CheckBox)Colorbar).IsEnabled = false;
            //else ((CheckBox)Colorbar).IsEnabled = false;
        }

        private void ClickedGenerate(object sender, RoutedEventArgs e)
        {

            Result.Source = (ImageSource)new ImageSourceConverter().ConvertFrom(assetsFolder + "waiting.png");

            /*
            if (File.Exists("../../../../output.png"))
            {
                if (Result.Source == (ImageSource)new ImageSourceConverter().ConvertFrom("../../../../output.png"))
                {
                    Result.Source = (ImageSource)new ImageSourceConverter().ConvertFrom(assetsFolder + "waiting.png");
                }
                File.Delete("../../../../output.png");
            }
            */

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
                       

            System.Diagnostics.Process process = new System.Diagnostics.Process();
            System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo
            {
                WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden,
                FileName = "cmd.exe",
                Arguments = command
            };
            process.StartInfo = startInfo;
            process.Start();
            process.WaitForExit();
            

            Result.Source = (ImageSource)new ImageSourceConverter().ConvertFrom("../../../../output.png");
            Generate.IsEnabled = false;
        }
    }
}