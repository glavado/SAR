decision_tree = {
    "screens": [
        "HomeScreen",
        "MinistrySARsScreen",
        "ReferBackToSchoolScreen",
        "ATSAvailableScreen",
        "ATSNotAvailableScreen",
        "RMAssessorScreen",
        "PKHistoricComponentMarksScreen",
        "ADARequestScreen",
        "ResponseScreen"
    ],
    "controls": {
        "HomeScreen": {
            "dropdowns": {
                "CountryDropdown": [
                    "MinistryCountry1",
                    "MinistryCountry2",
                    "China",
                    "Mauritius",
                    "Maldives",
                    "Pakistan",
                    "OtherCountry"
                ],
                "RequestTypeDropdown": [
                    "CMR",
                    "ATS",
                    "MCQ",
                    "Script Copy",
                    "Component Marks",
                    "Item Level"
                ],
                "SeriesDropdown": [
                    "J24",
                    "J25",
                    "M25",
                    "N21",
                    "J22",
                    "N22",
                    "J23",
                    "N23"
                ]
            },
            "datePicker": "RequestDatePicker",
            "button": "SubmitButton"
        },
        "ResponseScreen": {
            "label": "ResponseLabel"
        }
    },
    "logic": {
        "SubmitButton.OnSelect": [
            {
                "condition": "CountryDropdown.Selected.Value in ['MinistryCountry1', 'MinistryCountry2']",
                "action": "Navigate(MinistrySARsScreen)"
            },
            {
                "condition": "RequestTypeDropdown.Selected.Value == 'CMR' and SeriesDropdown.Selected.Value in ['J24', 'J25', 'M25']",
                "action": "Navigate(ReferBackToSchoolScreen)"
            },
            {
                "condition": "RequestTypeDropdown.Selected.Value == 'ATS' and SeriesDropdown.Selected.Value == 'J25' and CountryDropdown.Selected.Value not in ['China', 'Mauritius', 'Maldives']",
                "action": "Navigate(ATSAvailableScreen)"
            },
            {
                "condition": "RequestTypeDropdown.Selected.Value == 'ATS' and SeriesDropdown.Selected.Value == 'J25' and CountryDropdown.Selected.Value in ['China', 'Mauritius', 'Maldives']",
                "action": "Navigate(ATSNotAvailableScreen)"
            },
            {
                "condition": "RequestTypeDropdown.Selected.Value == 'Script Copy' and DateDiff(RequestDatePicker.SelectedDate, Today()) <= 11",
                "action": "Navigate(RMAssessorScreen)"
            },
            {
                "condition": "RequestTypeDropdown.Selected.Value == 'Script Copy' and DateDiff(RequestDatePicker.SelectedDate, Today()) > 11 and DateDiff(RequestDatePicker.SelectedDate, Today()) <= 18",
                "action": "Navigate(ResponseScreen); Set(ResponseText, 'Contact Leah Dark to confirm if we still hold this or if Archives do')"
            },
            {
                "condition": "RequestTypeDropdown.Selected.Value == 'Script Copy' and DateDiff(RequestDatePicker.SelectedDate, Today()) > 18",
                "action": "Navigate(ResponseScreen); Set(ResponseText, 'Scripts have been destroyed')"
            },
            {
                "condition": "RequestTypeDropdown.Selected.Value == 'MCQ'",
                "action": "Navigate(ADARequestScreen); Set(ResponseText, 'Send to CI Assessment Data and Analytics: CIAssessmentDataAndAnalytics@cambridge.org')"
            }
        ]
    }
}